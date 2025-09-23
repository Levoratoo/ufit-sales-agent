# UFIT Sales Agent - Script de Criação Automática do Repositório GitHub
# Execute este script no PowerShell

Write-Host "🚀 UFIT Sales Agent - Criação Automática do Repositório GitHub" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan

# Verificar se estamos no diretório correto
if (-not (Test-Path "main.py")) {
    Write-Host "❌ Execute este script na pasta do projeto UFIT Sales Agent!" -ForegroundColor Red
    exit 1
}

# Verificar configuração do Git
Write-Host "🔍 Verificando configuração do Git..." -ForegroundColor Yellow

$gitName = git config user.name
$gitEmail = git config user.email

if (-not $gitName) {
    $nome = Read-Host "Digite seu nome para o Git"
    git config --global user.name $nome
    Write-Host "✅ User.name configurado!" -ForegroundColor Green
}

if (-not $gitEmail) {
    $email = Read-Host "Digite seu email para o Git"
    git config --global user.email $email
    Write-Host "✅ User.email configurado!" -ForegroundColor Green
}

# Obter username do GitHub
$username = Read-Host "Digite seu username do GitHub"
if (-not $username) {
    Write-Host "❌ Username é obrigatório!" -ForegroundColor Red
    exit 1
}

$repoUrl = "https://github.com/$username/ufit-sales-agent.git"

Write-Host "`n🎯 Repositório será criado em: $repoUrl" -ForegroundColor Cyan
Write-Host "`n📋 INSTRUÇÕES:" -ForegroundColor Yellow
Write-Host "1. Acesse: https://github.com/new" -ForegroundColor White
Write-Host "2. Nome do repositório: ufit-sales-agent" -ForegroundColor White
Write-Host "3. Descrição: Agente de vendas inteligente para UFIT com sistema de aprovação automática" -ForegroundColor White
Write-Host "4. Marque como Público" -ForegroundColor White
Write-Host "5. NÃO marque 'Initialize with README'" -ForegroundColor White
Write-Host "6. Clique em 'Create repository'" -ForegroundColor White

Read-Host "`n⏳ Pressione ENTER quando tiver criado o repositório no GitHub"

# Executar comandos
Write-Host "`n🔄 Executando comandos..." -ForegroundColor Yellow

Write-Host "🔄 Conectando com repositório GitHub..." -ForegroundColor Yellow
git remote add origin $repoUrl
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Conectado com sucesso!" -ForegroundColor Green
} else {
    Write-Host "❌ Erro ao conectar. Verifique se o repositório foi criado." -ForegroundColor Red
    exit 1
}

Write-Host "🔄 Renomeando branch para main..." -ForegroundColor Yellow
git branch -M main
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Branch renomeada!" -ForegroundColor Green
} else {
    Write-Host "❌ Erro ao renomear branch." -ForegroundColor Red
}

Write-Host "🔄 Fazendo push dos arquivos..." -ForegroundColor Yellow
git push -u origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Push realizado com sucesso!" -ForegroundColor Green
    Write-Host "`n🎉 SUCESSO! Repositório criado e configurado!" -ForegroundColor Green
    Write-Host "🔗 Acesse: https://github.com/$username/ufit-sales-agent" -ForegroundColor Cyan
    Write-Host "`n📁 Seus arquivos estão agora no GitHub!" -ForegroundColor Green
} else {
    Write-Host "❌ Erro ao fazer push. Tente executar manualmente:" -ForegroundColor Red
    Write-Host "   git push -u origin main" -ForegroundColor White
}

Write-Host "`nPressione qualquer tecla para sair..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
