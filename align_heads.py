"""
align_heads.py  (PIL version)
Detecta o topo da cabeça detectando pixels não-fundo e alinha todas as fotos.
"""
from PIL import Image
import numpy as np
import os

PHOTOS_DIR = "team-photos"
BG_COLOR = np.array([24, 32, 40], dtype=np.float32)   # #182028 em RGB
BG_TOLERANCE = 35          # threshold de distância do fundo
HEAD_MARGIN_PX = 28        # margem acima do topo da cabeça
JPEG_QUALITY = 95

photos = [
    "FelipeGuinle.jpeg",
    "RodrigoCardoso.jpeg",
    "Celson.jpeg",
    "ViniciusAlmeida.jpeg",
    "DaniloBarbosa.jpeg",
    "FelipeRibeiro.jpeg",
    "ThiagoOtuki.jpeg",
    "MayconBrito.jpeg",
    "MoraisJr.jpeg",
]

def find_head_top(arr_rgb):
    """Retorna o Y do primeiro pixel que diverge do fundo."""
    diff = np.linalg.norm(arr_rgb.astype(np.float32) - BG_COLOR, axis=2)
    mask = diff > BG_TOLERANCE
    rows = np.where(mask.any(axis=1))[0]
    return int(rows[0]) if len(rows) > 0 else 0

# --- Passo 1: medir ---
print("Analisando imagens...")
data = []
for fname in photos:
    path = os.path.join(PHOTOS_DIR, fname)
    try:
        img = Image.open(path).convert("RGB")
    except Exception as e:
        print(f"  [SKIP] {fname}: {e}")
        continue
    arr = np.array(img)
    head_top = find_head_top(arr)
    print(f"  {fname}: topo da cabeça em y={head_top}  (altura={img.height})")
    data.append({"fname": fname, "img": img, "arr": arr, "head_top": head_top})

if not data:
    print("Nenhuma imagem carregada.")
    exit()

# --- Passo 2: calcular deslocamento alvo ---
max_head_top = max(d["head_top"] for d in data)
target_y = max_head_top + HEAD_MARGIN_PX
print(f"\nTopo-alvo: y={target_y}px  (maior topo={max_head_top} + margem={HEAD_MARGIN_PX})")

# --- Passo 3: reposicionar ---
bg_rgb = tuple(int(x) for x in BG_COLOR)  # (24, 32, 40)
print("\nReposicionando e salvando...")
for d in data:
    arr = d["arr"]
    h, w = arr.shape[:2]
    shift = target_y - d["head_top"]   # positivo = mover imagem para baixo

    if shift > 0:
        pad = np.full((shift, w, 3), bg_rgb, dtype=np.uint8)
        new_arr = np.vstack([pad, arr])[:h]
    elif shift < 0:
        new_arr = np.vstack([arr[-shift:], np.full((-shift, w, 3), bg_rgb, dtype=np.uint8)])[:h]
    else:
        new_arr = arr

    out = Image.fromarray(new_arr)
    out_path = os.path.join(PHOTOS_DIR, d["fname"])
    out.save(out_path, "JPEG", quality=JPEG_QUALITY)
    print(f"  {d['fname']}  shift={shift:+d}px  → salvo")

print("\nConcluído! Recarregue o browser.")
