"""Junta transcrições do whisper.cpp feitas em partes sobrepostas num arquivo só.

Uso:
    python juntar_partes_transcricao.py PASTA_PARTES SAIDA_BASE INICIO0 INICIO1 ... --sobreposicao 10

Cada parte `parte-N.json` (saída -oj do whisper.cpp) começa em INICIO_N segundos do
áudio original. Na sobreposição entre duas partes, o corte fica no meio: um segmento
pertence à parte em que começa antes desse ponto. Grava SAIDA_BASE.json, .srt e .txt
com tempos absolutos.
"""
import argparse
import json
from pathlib import Path


def tempo_srt(s):
    ms = int(round(s * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    seg, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{seg:02d},{ms:03d}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("pasta")
    p.add_argument("saida")
    p.add_argument("inicios", nargs="+", type=float)
    p.add_argument("--sobreposicao", type=float, default=10.0)
    a = p.parse_args()

    pasta = Path(a.pasta)
    cortes = [a.inicios[i] + a.sobreposicao / 2 for i in range(1, len(a.inicios))]
    limites = [(0.0 if i == 0 else cortes[i - 1], cortes[i] if i < len(cortes) else float("inf"))
               for i in range(len(a.inicios))]

    segmentos = []
    for i, ini in enumerate(a.inicios):
        dados = json.loads((pasta / f"parte-{i}.json").read_text(encoding="utf-8"))
        de, ate = limites[i]
        for s in dados["transcription"]:
            inicio = ini + s["offsets"]["from"] / 1000
            fim = ini + s["offsets"]["to"] / 1000
            if de <= inicio < ate:
                segmentos.append({"parte": i, "inicio": round(inicio, 3), "fim": round(fim, 3),
                                  "texto": s["text"].strip()})

    # O reconhecimento às vezes repete a mesma frase em série num trecho sem fala clara
    # (no caso Band, "A CIDADE NO BRASIL" 104 vezes). Uma série de 3 ou mais segmentos
    # idênticos vira um segmento só, marcado, e a série fica registrada na saída.
    series, limpos, i = [], [], 0
    while i < len(segmentos):
        j = i
        while j + 1 < len(segmentos) and segmentos[j + 1]["texto"] == segmentos[i]["texto"]:
            j += 1
        if j - i + 1 >= 3:
            series.append({"texto": segmentos[i]["texto"], "repeticoes": j - i + 1,
                           "inicio": segmentos[i]["inicio"], "fim": segmentos[j]["fim"]})
            limpos.append({**segmentos[i], "fim": segmentos[j]["fim"],
                           "texto": "[trecho sem transcrição confiável]"})
        else:
            limpos.extend(segmentos[i:j + 1])
        i = j + 1
    segmentos = limpos

    saida = Path(a.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.with_suffix(".json").write_text(
        json.dumps({"cortes_entre_partes": cortes, "series_repetidas": series, "segmentos": segmentos},
                   ensure_ascii=False, indent=1),
        encoding="utf-8")
    with saida.with_suffix(".srt").open("w", encoding="utf-8") as f:
        for n, s in enumerate(segmentos, 1):
            f.write(f"{n}\n{tempo_srt(s['inicio'])} --> {tempo_srt(s['fim'])}\n{s['texto']}\n\n")
    with saida.with_suffix(".txt").open("w", encoding="utf-8") as f:
        for s in segmentos:
            f.write(f"[{tempo_srt(s['inicio'])[:8]}] {s['texto']}\n")
    print(f"{len(segmentos)} segmentos; cortes entre partes em {cortes}")
    for s in series:
        print(f"série repetida: {s['repeticoes']}x de {s['inicio']} a {s['fim']} s: {s['texto'][:60]}")


if __name__ == "__main__":
    main()
