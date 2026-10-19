"""Reconta os detalhes verificáveis de cada compromisso e os temas por candidato."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

CAMPOS = ("mecanismo", "instituicao", "prazo_meta", "recurso_custo", "condicao_legal")


def calcular(compromissos: Path, detalhes: Path) -> dict:
    with compromissos.open(encoding="utf-8", newline="") as f:
        base = {l["id"]: l for l in csv.DictReader(f)}
    with detalhes.open(encoding="utf-8", newline="") as f:
        linhas = list(csv.DictReader(f))
    ids = [l["id"] for l in linhas]
    if len(ids) != len(set(ids)) or set(ids) != set(base):
        raise ValueError("DETALHES_COMPROMISSOS.csv não cobre exatamente os compromissos")
    por_campo = {p: Counter() for p in ("flavio", "lula")}
    por_numero = {p: Counter() for p in ("flavio", "lula")}
    temas = {p: Counter() for p in ("flavio", "lula")}
    total = Counter()
    for l in linhas:
        autor = base[l["id"]]["autor"]
        total[autor] += 1
        temas[autor][base[l["id"]]["tema"]] += 1
        presentes = 0
        for c in CAMPOS:
            valor = l[c].strip()
            if valor != "nao":
                if ":" not in valor.split(" ", 1)[0]:
                    raise ValueError(f"{l['id']}.{c}: detalhe presente precisa começar pelo tempo mm:ss")
                por_campo[autor][c] += 1
                presentes += 1
        por_numero[autor][presentes] += 1
    return {
        "unidade": "compromisso distinto do COMPROMISSOS.csv; campo presente só com palavras na fala e tempo",
        "compromissos": dict(total),
        "campo_presente": {p: {c: por_campo[p][c] for c in CAMPOS} for p in por_campo},
        "compromissos_por_numero_de_campos": {p: {str(k): v for k, v in sorted(c.items())} for p, c in por_numero.items()},
        "temas": {p: dict(sorted(c.items(), key=lambda x: (-x[1], x[0]))) for p, c in temas.items()},
    }


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("compromissos", type=Path)
    a.add_argument("detalhes", type=Path)
    a.add_argument("saida", type=Path)
    args = a.parse_args()
    args.saida.write_text(json.dumps(calcular(args.compromissos, args.detalhes), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
