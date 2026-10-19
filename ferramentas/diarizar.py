"""Gera pistas acústicas de falante a partir de exemplos identificados no vídeo.

Não substitui a revisão dos limites de turno. Requer `resemblyzer`, `numpy`
e o WAV mono PCM 16 kHz extraído do vídeo de trabalho. A saída é local.
"""

from __future__ import annotations

import argparse
import json
import wave
from pathlib import Path

import numpy as np
from resemblyzer import VoiceEncoder


EXEMPLOS = {
    "flavio": [(300, 315), (330, 345), (615, 630), (3360, 3375),
               (4470, 4485), (5325, 5340), (5730, 5745)],
    "lula": [(410, 425), (450, 465), (560, 575), (3980, 3995),
             (4280, 4295), (5180, 5195), (6200, 6215), (6530, 6545)],
}
JANELAS_DEBATE = [(195, 2765), (3210, 4580), (5030, 6740)]


def ler_wav(caminho: Path) -> np.ndarray:
    with wave.open(str(caminho), "rb") as audio:
        if (audio.getframerate(), audio.getnchannels(), audio.getsampwidth()) != (16000, 1, 2):
            raise ValueError("WAV deve ser PCM mono de 16 kHz e 16 bits")
        return np.frombuffer(audio.readframes(audio.getnframes()), dtype="<i2").astype(np.float32) / 32768


def executar(wav: Path, saida: Path, passo: float = 2.0, janela: float = 3.0) -> None:
    amostras = ler_wav(wav)
    encoder = VoiceEncoder(device="cpu")
    centros = {}
    for pessoa, intervalos in EXEMPLOS.items():
        vetores = [encoder.embed_utterance(amostras[int(a*16000):int(b*16000)])
                   for a, b in intervalos]
        centro = np.mean(vetores, axis=0)
        centros[pessoa] = centro / np.linalg.norm(centro)

    dados = []
    for ini, fim in JANELAS_DEBATE:
        t = float(ini)
        while t + janela <= min(fim, len(amostras) / 16000):
            parte = amostras[int(t*16000):int((t+janela)*16000)]
            rms = float(np.sqrt(np.mean(parte*parte)))
            if rms < 0.007:
                dados.append({"inicio_s": t, "fim_s": t+janela, "rotulo": "silencio",
                              "rms": round(rms, 4)})
                t += passo
                continue
            vetor = encoder.embed_utterance(parte)
            scores = {p: float(vetor @ centro) for p, centro in centros.items()}
            ordem = sorted(scores, key=scores.get, reverse=True)
            margem = scores[ordem[0]] - scores[ordem[1]]
            rotulo = ordem[0] if scores[ordem[0]] >= 0.82 and margem >= 0.04 else "incerto"
            dados.append({"inicio_s": t, "fim_s": t+janela, "rotulo": rotulo,
                          "scores": {k: round(v, 3) for k, v in scores.items()},
                          "margem": round(margem, 3), "rms": round(rms, 4)})
            t += passo

    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(json.dumps({"motor": "Resemblyzer 0.1.4", "passo_s": passo,
                                 "janela_s": janela, "exemplos_s": EXEMPLOS,
                                 "janelas_debate_s": JANELAS_DEBATE,
                                 "limiar_coseno": 0.82, "limiar_margem": 0.04,
                                 "janelas": dados}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("wav", type=Path)
    parser.add_argument("saida", type=Path)
    args = parser.parse_args()
    executar(args.wav, args.saida)
