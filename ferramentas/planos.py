"""Agrupa enquadramentos para orientar a atribuição humana de turnos.

Inspirado no rascunho-de-turnos do projeto checagem-eleicoes-2026 (MIT).
Clusters são pistas visuais, nunca identificação final de falante.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def executar(video: Path, destino: Path, grupos: int = 20, fps: int = 1) -> None:
    destino.mkdir(parents=True, exist_ok=True)
    pequeno = (32, 18)
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(video),
           "-vf", f"fps={fps},scale={pequeno[0]}:{pequeno[1]}", "-f", "rawvideo",
           "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    quadros = np.frombuffer(raw, dtype=np.uint8).reshape(-1, pequeno[0] * pequeno[1] * 3)
    x = quadros.astype(np.float32) / 255.0
    norma_x = (x * x).sum(axis=1)
    rng = np.random.default_rng(20261019)
    centroides = x[rng.choice(len(x), grupos, replace=False)].copy()
    for _ in range(24):
        dist = norma_x[:, None] + (centroides * centroides).sum(axis=1)[None, :] - 2 * x @ centroides.T
        rotulos = dist.argmin(axis=1)
        for g in range(grupos):
            if np.any(rotulos == g):
                centroides[g] = x[rotulos == g].mean(axis=0)
    dist = norma_x[:, None] + (centroides * centroides).sum(axis=1)[None, :] - 2 * x @ centroides.T
    rotulos = dist.argmin(axis=1)
    (destino / "planos.json").write_text(json.dumps({
        "fps": fps, "grupos": grupos, "semente": 20261019,
        "rotulo_por_quadro": rotulos.tolist(),
    }, ensure_ascii=False) + "\n", encoding="utf-8")

    thumb = (256, 144)
    margem = 170
    rows_per_sheet = 10
    for inicio in range(0, grupos, rows_per_sheet):
        fim = min(inicio + rows_per_sheet, grupos)
        folha = Image.new("RGB", (margem + 4 * thumb[0], (fim - inicio) * (thumb[1] + 10)), "#171717")
        draw = ImageDraw.Draw(folha)
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
        for g in range(inicio, fim):
            idx = np.flatnonzero(rotulos == g)
            y = (g - inicio) * (thumb[1] + 10)
            draw.text((8, y + 8), f"Plano {g}", font=font, fill="white")
            draw.text((8, y + 34), f"{len(idx)/fps/60:.1f} min", font=font, fill="white")
            if not len(idx):
                continue
            ordenados = idx[np.argsort(dist[idx, g])]
            escolhas = [int(ordenados[min(int(q * (len(ordenados) - 1)), len(ordenados)-1)])
                        for q in (0.02, 0.15, 0.45, 0.75)]
            for col, numero in enumerate(escolhas):
                instante = numero / fps
                cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", str(instante),
                       "-i", str(video), "-frames:v", "1", "-vf",
                       f"scale={thumb[0]}:{thumb[1]}", "-f", "image2pipe", "-vcodec", "mjpeg", "-"]
                data = subprocess.run(cmd, check=True, capture_output=True).stdout
                import io
                quadro = Image.open(io.BytesIO(data)).convert("RGB")
                folha.paste(quadro, (margem + col * thumb[0], y))
                h = int(instante) // 3600
                m = (int(instante) % 3600) // 60
                s = int(instante) % 60
                draw.text((margem + col * thumb[0] + 4, y + thumb[1] - 25),
                          f"{h:02d}:{m:02d}:{s:02d}", font=font, fill="#ffffff",
                          stroke_width=2, stroke_fill="#000000")
        folha.save(destino / f"planos-{inicio:02d}-{fim-1:02d}.jpg", quality=85)
    print(f"{len(rotulos)} quadros, {grupos} grupos, folhas em {destino}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("destino", type=Path)
    parser.add_argument("--grupos", type=int, default=20)
    parser.add_argument("--fps", type=int, default=1)
    args = parser.parse_args()
    executar(args.video, args.destino, args.grupos, args.fps)
