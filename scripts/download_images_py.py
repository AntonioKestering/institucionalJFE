"""
Baixa imagens do Unsplash para ./assets/images usando Python (sem dependências externas).
Uso: python scripts/download_images_py.py
"""
import urllib.request
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_ROOT / 'assets' / 'images'
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

images = [
    ("https://source.unsplash.com/1600x900/?luxury,spa", "hero-spa.jpg"),
    ("https://source.unsplash.com/1200x800/?luxury,interior", "environment-1.jpg"),
    ("https://source.unsplash.com/1200x800/?wellness,spa,room", "environment-2.jpg"),
    ("https://source.unsplash.com/800x600/?microagulhamento", "service-micro.jpg"),
    ("https://source.unsplash.com/800x600/?limpeza,facial", "service-facial.jpg"),
    ("https://source.unsplash.com/800x600/?preenchimento,labios", "service-lips.jpg"),
    ("https://source.unsplash.com/800x600/?peeling,chemical", "service-peeling.jpg"),
    ("https://source.unsplash.com/400x400/?woman,portrait,beauty", "testimonial-1.jpg"),
    ("https://source.unsplash.com/400x400/?woman,happy,smile", "testimonial-2.jpg")
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
