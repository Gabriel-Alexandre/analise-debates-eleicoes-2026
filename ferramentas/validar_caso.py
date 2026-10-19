"""Confere integridade dos resultados publicados; não audita o áudio."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

from contar_oportunidades import calcular
from selecionar_propostas import ordenar


RESULTADOS_VALIDOS = {
    "caminho identificado",
    "depende de condição documentada",
    "não há caminho demonstrado com as fontes localizadas",
    "indeterminado por dado ausente",
}


def validar(raiz: Path, caso: Path) -> list[str]:
    erros = []
    metodo = raiz / "docs" / "FONTES.md"
    fontes = metodo.read_text(encoding="utf-8")
    a = caso / "anotacoes"
    r = caso / "resultados"
    esperado_c = json.loads(json.dumps(ordenar(a / "COMPROMISSOS.csv"), ensure_ascii=False))
    publicado_c = json.loads((r / "SELECAO_C.json").read_text(encoding="utf-8"))
    if esperado_c != publicado_c:
        erros.append("SELECAO_C.json diverge das anotações")
    esperado_b = calcular(a / "OPORTUNIDADES.md")
    publicado_b = json.loads((r / "RESPOSTAS.json").read_text(encoding="utf-8"))
    if esperado_b != publicado_b:
        erros.append("RESPOSTAS.json diverge das oportunidades")
    selecionados = {ident for lista in esperado_c["selecionados"].values() for ident in lista}
    with (r / "CONDICOES_C.csv").open(encoding="utf-8", newline="") as arquivo:
        linhas = list(csv.DictReader(arquivo))
    ids = [linha["id"] for linha in linhas]
    if len(ids) != len(set(ids)) or set(ids) != selecionados:
        erros.append("CONDICOES_C.csv não corresponde exatamente às quatro ações selecionadas")
    for linha in linhas:
        if linha["resultado"] not in RESULTADOS_VALIDOS:
            erros.append(f"resultado inválido em {linha['id']}")
        for fonte in linha["fontes"].split(";"):
            if f"| {fonte} |" not in fontes:
                erros.append(f"fonte {fonte} ausente em FONTES.md")
    texto_relatorio = (caso / "RELATORIO.md").read_text(encoding="utf-8")
    for ident in selecionados:
        if f"**{ident};" not in texto_relatorio:
            erros.append(f"{ident} ausente do relatório")
    for documento in (raiz / "README.md", caso / "RELATORIO.md", caso / "RESUMO_SIMPLES.md",
                      caso / "REPRODUCAO.md"):
        for destino in re.findall(r"\]\(([^)]+)\)", documento.read_text(encoding="utf-8")):
            if destino.startswith(("http://", "https://", "#")):
                continue
            caminho = (documento.parent / destino.split("#", 1)[0]).resolve()
            if not caminho.exists():
                erros.append(f"link local quebrado: {documento.name}: {destino}")
    return erros


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("caso", type=Path)
    args = parser.parse_args()
    raiz = Path(__file__).resolve().parents[1]
    falhas = validar(raiz, args.caso.resolve())
    if falhas:
        raise SystemExit("\n".join(falhas))
    print("Integridade dos resultados: OK (sem auditoria do áudio)")
