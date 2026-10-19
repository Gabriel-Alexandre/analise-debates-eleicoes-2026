"""Reconta as classificações da tabela pública de oportunidades."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def calcular(caminho: Path) -> dict:
    grupos: dict[str, dict[str, Counter]] = {
        "perguntas_iguais": {"flavio": Counter(), "lula": Counter()},
        "confronto_livre": {"flavio": Counter(), "lula": Counter()},
        "confronto_estruturado": {"flavio": Counter(), "lula": Counter()},
    }
    tipos: dict[str, dict[str, Counter]] = {
        "confronto_livre": {"flavio": Counter(), "lula": Counter()},
        "confronto_estruturado": {"flavio": Counter(), "lula": Counter()},
    }
    vistos = set()
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        if not linha.startswith("| M") and not linha.startswith("| C"):
            continue
        campos = [c.strip() for c in linha.strip("| ").split("|")]
        ident = campos[0]
        if ident in vistos or ident[0] not in "MC":
            raise ValueError(f"ID duplicado/inválido: {ident}")
        vistos.add(ident)
        if ident.startswith("M"):
            for pessoa, pos in (("flavio", 3), ("lula", 4)):
                classe = campos[pos]
                if classe not in "DPNI":
                    raise ValueError((ident, classe))
                grupos["perguntas_iguais"][pessoa][classe] += 1
        else:
            grupo = "confronto_estruturado" if 9 <= int(ident[1:]) <= 12 else "confronto_livre"
            destino = campos[2].split("→")[-1].strip().lower()
            pessoa = "flavio" if destino.startswith("flávio") else "lula" if destino.startswith("lula") else None
            classe = campos[4]
            if not pessoa or classe not in "DPNI":
                raise ValueError((ident, destino, classe))
            grupos[grupo][pessoa][classe] += 1
            # tipo do núcleo, contado por quem PERGUNTOU
            autor = campos[2].split("→")[0].strip().lower()
            perguntou = "flavio" if autor.startswith("flávio") else "lula" if autor.startswith("lula") else None
            tipo = campos[6] if len(campos) > 6 else ""
            if not perguntou or tipo not in {"politica", "posicao", "conduta"}:
                raise ValueError((ident, autor, tipo))
            tipos[grupo][perguntou][tipo] += 1
    if len(vistos) != 34:
        raise ValueError(f"esperados 34 componentes, encontrados {len(vistos)}")
    saida = {g: {p: {k: v for k, v in sorted(c.items())} for p,c in pessoas.items()}
             for g,pessoas in grupos.items()}
    saida["tipo_das_perguntas_por_quem_perguntou"] = {
        g: {p: {k: v for k, v in sorted(c.items())} for p, c in pessoas.items()}
        for g, pessoas in tipos.items()}
    return saida


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("entrada", type=Path)
    p.add_argument("saida", type=Path)
    a = p.parse_args()
    a.saida.parent.mkdir(parents=True, exist_ok=True)
    a.saida.write_text(json.dumps(calcular(a.entrada), ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
