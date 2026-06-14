"""
Script Python para gerar variantes WebP e resized das imagens em ./assets/images
Requisitos: Python 3.8+ e Pillow
Instalação: pip install pillow
Uso: python scripts/convert_images_py.py
"""
from PIL import Image
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_ROOT / 'assets' / 'images'

# Names to process - pattern matching
patterns = ['hero-spa.jpg', 'environment-1.jpg', 'environment-2.jpg']
patterns += list(ASSETS_DIR.glob('service-*.jpg'))

# Sizes (widths)
sizes = [1600, 1200, 800, 400]
quality = 80

if not ASSETS_DIR.exists():
    print(f'Pasta não encontrada: {ASSETS_DIR}')
    raise SystemExit(1)

# Prepare list of files (Path objects)
files = []
for p in patterns:
    if isinstance(p, Path):
        if p.exists():
            files.append(p)
    else:
        fp = ASSETS_DIR / p
        if fp.exists():
            files.append(fp)

# Also include any other jpg/jpeg files in the folder
for f in ASSETS_DIR.glob('*.jpg'):
    if f not in files:
        files.append(f)

if not files:
    print('Nenhum arquivo .jpg encontrado em:', ASSETS_DIR)
    raise SystemExit(0)

print('Arquivos a processar:')
for f in files:
    print(' -', f.name)

for file in files:
    try:
        img = Image.open(file)
        img = img.convert('RGB')
        base = file.stem

        # Save original-size webp
        out_webp = file.with_suffix('.webp')
        img.save(out_webp, 'WEBP', quality=quality)
        print(f'Gerado {out_webp.name}')

        for w in sizes:
            # compute resized height maintaining aspect ratio
            ratio = w / img.width
            if ratio >= 1:
                # don't upscale; skip creating larger sizes
                continue
            new_h = int(img.height * ratio)
            resized = img.resize((w, new_h), Image.LANCZOS)
            out_webp_resized = ASSETS_DIR / f"{base}-{w}.webp"
            resized.save(out_webp_resized, 'WEBP', quality=quality)
            out_jpg_resized = ASSETS_DIR / f"{base}-{w}.jpg"
            resized.save(out_jpg_resized, 'JPEG', quality=84)
            print(f'Gerado {out_webp_resized.name} e {out_jpg_resized.name}')

    except Exception as e:
        print(f'Erro processando {file.name}:', e)

print('Concluído.')
