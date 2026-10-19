"""Aplica a regra temporal do pré-registro sem consultar fontes externas."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def segundos(texto: str) -> int:
    m, s = (int(v) for v in texto.split(":"))
    if s >= 60:
        raise ValueError(texto)
    return 60*m+s


def ordenar(caminho: Path) -> dict:
    linhas = list(csv.DictReader(caminho.open(encoding="utf-8", newline="")))
    if len({x["id"] for x in linhas}) != len(linhas):
        raise ValueError("IDs de compromisso repetidos")
    registro = []
    for linha in linhas:
        partes = []
        for trecho in linha["ocorrencias"].split(";"):
            a, b = (segundos(v) for v in trecho.split("-"))
            if not 0 <= a < b <= 6855:
                raise ValueError(f"tempo inválido: {linha['id']}: {trecho}")
            partes.append((a, b))
        partes.sort()
        if any(b > c for (_, b), (c, _) in zip(partes, partes[1:])):
            raise ValueError(f"sobreposição no mesmo compromisso: {linha['id']}")
        registro.append({"id": linha["id"], "autor": linha["autor"], "tema": linha["tema"],
                         "acao_resumida": linha["acao_resumida"],
                         "elegivel_c": linha["elegivel_c"] == "sim",
                         "ocorrencias_s": partes, "tempo_apresentacao_s": sum(b-a for a,b in partes),
                         "numero_ocorrencias": len(partes), "primeira_aparicao_s": partes[0][0]})
    ranking = {}
    for pessoa in ("flavio", "lula"):
        ranking[pessoa] = sorted((r for r in registro if r["autor"] == pessoa and r["elegivel_c"]),
                                 key=lambda r: (-r["tempo_apresentacao_s"],
                                                -r["numero_ocorrencias"], r["primeira_aparicao_s"]))
    return {"regra": "até duas ações elegíveis por autor; duração dos intervalos anotados; desempate: ocorrências, depois primeira aparição",
            "todos": registro, "selecionados": {p: [r["id"] for r in lista[:2]] for p, lista in ranking.items()},
            "ranking_elegiveis": {p: [r["id"] for r in lista] for p, lista in ranking.items()}}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("csv", type=Path)
    p.add_argument("saida", type=Path)
    args = p.parse_args()
    result = ordenar(args.csv)
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(result["selecionados"])
