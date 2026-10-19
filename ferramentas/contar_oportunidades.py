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
            grupo = "confronto_livre" if int(ident[1:]) <= 8 else "confronto_estruturado"
            destino = campos[2].split("→")[-1].strip().lower()
            pessoa = "flavio" if destino.startswith("flávio") else "lula" if destino.startswith("lula") else None
            classe = campos[4]
            if not pessoa or classe not in "DPNI":
                raise ValueError((ident, destino, classe))
            grupos[grupo][pessoa][classe] += 1
    if len(vistos) != 18:
        raise ValueError(f"esperados 18 componentes, encontrados {len(vistos)}")
    return {g: {p: {k: v for k, v in sorted(c.items())} for p,c in pessoas.items()}
            for g,pessoas in grupos.items()}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("entrada", type=Path)
    p.add_argument("saida", type=Path)
    a = p.parse_args()
    a.saida.parent.mkdir(parents=True, exist_ok=True)
    a.saida.write_text(json.dumps(calcular(a.entrada), ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
