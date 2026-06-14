# Script PowerShell para baixar imagens de placeholder do Unsplash
# Salva imagens em ./assets/images/

$projectPath = Join-Path $PSScriptRoot ".."
$assetsPath = Join-Path $projectPath "assets\images"

# Criar pasta se não existir
if (-not (Test-Path $assetsPath)) {
  New-Item -ItemType Directory -Force -Path $assetsPath | Out-Null
  Write-Host "Criado: $assetsPath"
}

$images = @(
  @{ url = "https://source.unsplash.com/1600x900/?luxury,spa"; name = "hero-spa.jpg" },
  @{ url = "https://source.unsplash.com/1200x800/?luxury,interior"; name = "environment-1.jpg" },
  @{ url = "https://source.unsplash.com/1200x800/?wellness,spa,room"; name = "environment-2.jpg" },
  @{ url = "https://source.unsplash.com/800x600/?microagulhamento"; name = "service-micro.jpg" },
  @{ url = "https://source.unsplash.com/800x600/?limpeza,facial"; name = "service-facial.jpg" },
  @{ url = "https://source.unsplash.com/800x600/?preenchimento,labios"; name = "service-lips.jpg" },
  @{ url = "https://source.unsplash.com/800x600/?peeling,chemical"; name = "service-peeling.jpg" },
  @{ url = "https://source.unsplash.com/400x400/?woman,portrait,beauty"; name = "testimonial-1.jpg" },
  @{ url = "https://source.unsplash.com/400x400/?woman,happy,smile"; name = "testimonial-2.jpg" }
)

Write-Host "Iniciando download das imagens para: $assetsPath`n"

foreach ($img in $images) {
  $outPath = Join-Path $assetsPath $img.name
  try {
    Write-Host "Baixando $($img.url) -> $($img.name)"
    Invoke-WebRequest -Uri $img.url -OutFile $outPath -UseBasicParsing -ErrorAction Stop
    Write-Host "✓ $($img.name) salvo"
  } catch {
    Write-Host "✗ Erro ao baixar $($img.url): $_"
  }
}

Write-Host "\nDownload concluído. Verifique a pasta: $assetsPath"
