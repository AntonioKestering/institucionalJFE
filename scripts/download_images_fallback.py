"""
Fallback downloader: usa Picsum.photos para obter imagens placeholder quando Unsplash estiver indisponível.
Uso: python scripts/download_images_fallback.py
"""
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_ROOT / 'assets' / 'images'
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

images = [
    ("https://picsum.photos/1600/900", "hero-spa.jpg"),
    ("https://picsum.photos/1200/800", "environment-1.jpg"),
    ("https://picsum.photos/1200/800", "environment-2.jpg"),
    ("https://picsum.photos/800/600", "service-micro.jpg"),
    ("https://picsum.photos/800/600", "service-facial.jpg"),
    ("https://picsum.photos/800/600", "service-lips.jpg"),
    ("https://picsum.photos/800/600", "service-peeling.jpg"),
    ("https://picsum.photos/400/400", "testimonial-1.jpg"),
    ("https://picsum.photos/400/400", "testimonial-2.jpg")
]

print(f"Salvando em: {ASSETS_DIR}")
for url, name in images:
    out_path = ASSETS_DIR / name
    try:
        print(f"Baixando: {url} -> {name}")
        urllib.request.urlretrieve(url, out_path)
        print(f"✓ {name}")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")

print("Concluído.")
