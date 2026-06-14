# Joice Folis Estética — Landing Page

Este repositório contém a Landing Page estática para `Joice Folis Estética` (HTML/CSS/JS). Projetada para publicação no GitHub Pages.

## Estrutura relevante

- `index.html` — arquivo principal (HTML, CSS e JS inline)
- `assets/images/` — imagens (JPEG baixadas do Unsplash)
- `scripts/convert-images.ps1` — script PowerShell para gerar variantes WebP e resized (ver seção abaixo)

## Passo A — Gerar WebP e variantes (recomendado para produção)

O projeto inclui um script PowerShell (`scripts/convert-images.ps1`) que gera versões WebP e imagens redimensionadas (1600, 1200, 800, 400 px) usando ImageMagick (`magick`) ou `cwebp` (libwebp).

Requisitos:
- Windows PowerShell
- ImageMagick (`magick`) preferido: https://imagemagick.org
- Alternativa: `cwebp` (libwebp): https://developers.google.com/speed/webp/download

Como usar:

1. Abra PowerShell no diretório do projeto (onde está este README).

```powershell
cd C:\Users\tonin\SiteJoiceFolisEstetica
.
```

2. Execute o script:

```powershell
cd scripts
.\convert-images.ps1
```

**Observação:** se você ainda não baixou as imagens para `./assets/images/` execute antes o script que baixa os placeholders do Unsplash:

```powershell
cd scripts
.\download-images.ps1
```

Isso criará os arquivos JPEG necessários (`hero-spa.jpg`, `service-*.jpg`, etc.) dentro de `./assets/images/` — depois execute `convert-images.ps1` para gerar as variantes WebP/redimensionadas.

Se o Unsplash estiver indisponível (HTTP 503) você pode usar o fallback com Picsum (mais estável para placeholders):

```powershell
cd scripts
python .\download_images_fallback.py
```

O script `download_images_fallback.py` baixa imagens do `picsum.photos` para os mesmos nomes de arquivo esperados e funciona sem necessidade de PowerShell (usa Python). Depois rode `convert_images_py.py` como descrito anteriormente.

O script procura por imagens com nomes: `hero-spa.jpg`, `environment-1.jpg`, `environment-2.jpg`, `service-*.jpg` dentro de `./assets/images/` e gera arquivos WebP e versões redimensionadas com sufixos `-1600`, `-1200`, `-800`, `-400`.

Exemplo de arquivos gerados:

- `hero-spa-1600.webp`, `hero-spa-1200.webp`, `hero-spa-800.webp`, `hero-spa.webp`
- `service-micro-800.webp`, `service-micro-400.webp`, etc.

Observação: se você não tiver ImageMagick, instale-o primeiro para obter redimensionamento automático.

## Passo D — Deploy no GitHub Pages

1. Crie um repositório no GitHub (por exemplo `username.github.io` para publicação no domínio raiz, ou qualquer repo para publicar via branch `gh-pages` ou `main`).
2. Adicione e comite os arquivos:

```powershell
git init
git add .
git commit -m "Initial landing page"
git branch -M main
git remote add origin https://github.com/<seu-usuario>/<repo>.git
git push -u origin main
```

3. No GitHub: vá em *Settings > Pages* e selecione a branch `main` e a pasta `/ (root)` como fonte. Salve.

4. Aguarde alguns minutos; o site estará disponível em `https://<seu-usuario>.github.io/<repo>/` (ou `https://<seu-usuario>.github.io/` se repo for `username.github.io`).

### Recomendações de produção

- Execute `scripts/convert-images.ps1` para gerar WebP e imagens otimizadas e use o `index.html` com `<picture>` (já preparado) para servir WebP onde suportado.
- Preload de fontes: se desejar, adicione `<link rel="preload" href="..." as="font" type="font/woff2" crossorigin>` quando usar self-hosting de fontes.
- Habilite HTTPS no GitHub Pages (ativado por padrão).
- Use `CNAME` se quiser domínio personalizado.
- Configure `robots.txt` / `sitemap.xml` e `Privacy Policy` se for coletar dados via Formspree.

## Testes locais

- Para servir localmente (evita problemas de recursos relativos):

```powershell
python -m http.server 8000
# abra http://localhost:8000
```

- Verifique:
  - Menu mobile (hamburger) abre/fecha.
  - Animações GSAP/Lenis funcionam no desktop; parallax desativado em mobile/touch.
  - Imagens abaixo da dobra carregam lazy (ver Network tab).

## Próximos passos recomendados

- Habilitar Formspree para formulário de contato.
- Gerar versões WebP e `srcset` (já preparado pelo script).
- Otimizar SEO: metatags Open Graph, structured data, sitemap.

Se quiser, eu executo os próximos passos: (1) rodar o script de conversão de imagens localmente (prefere que eu gere comandos detalhados?), (2) criar o formulário Formspree e integrar no `index.html`, (3) preparar deploy automático via GitHub Actions.