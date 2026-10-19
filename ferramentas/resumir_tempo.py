"""Reconta cobertura acústica por etapa a partir das janelas locais."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ETAPAS = [
    ("perguntas_iniciais", 195, 753),
    ("confronto_livre", 753, 2765),
    ("pergunta_saude", 3210, 3600),
    ("confronto_2", 3600, 4580),
    ("pergunta_produtividade", 5030, 5400),
    ("confronto_3", 5400, 6360),
    ("consideracoes_finais", 6360, 6740),
]


def resumir(entrada: Path) -> dict:
    bruto = json.loads(entrada.read_text(encoding="utf-8"))
    passo = bruto["passo_s"]
    janelas = bruto["janelas"]
    etapas = []
    for nome, inicio, fim in ETAPAS:
        contagens = Counter(j["rotulo"] for j in janelas if inicio <= j["inicio_s"] < fim)
        etapas.append({"nome": nome, "inicio_s": inicio, "fim_s": fim,
                       "segundos_janelas": {r: int(contagens[r] * passo)
                                            for r in ("flavio", "lula", "incerto", "silencio")}})
    totais = Counter()
    for etapa in etapas:
        totais.update(etapa["segundos_janelas"])
    return {"unidade": "rótulo de janela a cada 2 s; não é cronometragem manual de cada frase",
            "amostra_visual": "1039 de 1044 janelas com plano visual puro concordaram com o rótulo acústico; planos mistos excluídos",
            "aviso": "incerto inclui mediadores, silêncios curtos, transições e sobreposições; números de candidato são apenas fala atribuível neste procedimento",
            "etapas": etapas, "totais_segundos_janelas": dict(totais)}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("entrada", type=Path)
    p.add_argument("saida", type=Path)
    args = p.parse_args()
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_text(json.dumps(resumir(args.entrada), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
