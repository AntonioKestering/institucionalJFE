# Image conversion script for Windows PowerShell
# Generates WebP and resized JPEG/WebP variants for production.
# Requirements: ImageMagick (magick) or libwebp cwebp. Use ImageMagick if available.

$srcDir = Join-Path $PSScriptRoot "..\assets\images"
$dstDir = $srcDir

if (-not (Test-Path $srcDir)) {
  Write-Error "Source directory not found: $srcDir"
  exit 1
}

# Tools detection
$hasMagick = (Get-Command magick -ErrorAction SilentlyContinue) -ne $null
$hasCwebp = (Get-Command cwebp -ErrorAction SilentlyContinue) -ne $null

if (-not ($hasMagick -or $hasCwebp)) {
  Write-Host "Nenhuma ferramenta de conversão encontrada. Instale ImageMagick (magick) ou libwebp (cwebp)."
  Write-Host "ImageMagick: https://imagemagick.org/script/download.php"
  Write-Host "libwebp (cwebp): https://developers.google.com/speed/webp/download"
  exit 1
}

# Files to process (pattern for ones we've downloaded)
$files = Get-ChildItem -Path $srcDir -Include "hero-spa.jpg","environment-1.jpg","environment-2.jpg","service-*.jpg" -File -ErrorAction SilentlyContinue

if (-not $files) {
  Write-Host "Nenhum arquivo correspondente encontrado em $srcDir"
  exit 0
}

# Sizes map: name suffix -> width
$sizes = @(
  @{ suffix = "-1600"; width = 1600 },
  @{ suffix = "-1200"; width = 1200 },
  @{ suffix = "-800"; width = 800 },
  @{ suffix = "-400"; width = 400 }
)

foreach ($file in $files) {
  $base = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
  $ext = $file.Extension.ToLower()
  Write-Host "Processing $($file.Name)..."

  foreach ($size in $sizes) {
    $w = $size.width
    $suf = $size.suffix
    $outJpg = Join-Path $dstDir "${base}${suf}.jpg"
    $outWebp = Join-Path $dstDir "${base}${suf}.webp"

    if ($hasMagick) {
      # Resize and save JPEG
      magick convert "$($file.FullName)" -resize "${w}>" -strip -quality 84 "$outJpg"
      # Convert to WebP
      magick convert "$outJpg" -quality 80 "$outWebp"
    } elseif ($hasCwebp) {
      # Create resized JPG via magick if available; otherwise create WebP directly with cwebp (no resize)
      Write-Host "cwebp present but magick not found: creating webp from original (no resize)."
      $outWebpDirect = Join-Path $dstDir "${base}${suf}.webp"
      & cwebp -q 80 "$($file.FullName)" -o "$outWebpDirect"
    }
  }

  # Also create a default webp at original size
  $outWebpOrig = Join-Path $dstDir "${base}.webp"
  if ($hasMagick) {
    magick convert "$($file.FullName)" -strip -quality 80 "$outWebpOrig"
  } elseif ($hasCwebp) {
    & cwebp -q 80 "$($file.FullName)" -o "$outWebpOrig"
  }
}

Write-Host "Concluído. Verifique os arquivos gerados em: $srcDir"
