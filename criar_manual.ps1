# Script para criar repositório manualmente mas automatizado
Write-Host "🚀 UFIT Sales Agent - Criação do Repositório GitHub" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan

# Verificar se estamos no diretório correto
if (-not (Test-Path "main.py")) {
    Write-Host "❌ Execute este script na pasta do projeto UFIT Sales Agent!" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Projeto encontrado!" -ForegroundColor Green

# Verificar configuração do Git
Write-Host "`n🔍 Verificando configuração do Git..." -ForegroundColor Yellow

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

Write-Host "`n📋 INSTRUÇÕES MANUAIS:" -ForegroundColor Yellow
Write-Host "1. Acesse: https://github.com/new" -ForegroundColor White
Write-Host "2. Nome do repositório: ufit-sales-agent" -ForegroundColor White
Write-Host "3. Descrição: Agente de vendas inteligente para UFIT com sistema de aprovação automática" -ForegroundColor White
Write-Host "4. Marque como Público" -ForegroundColor White
Write-Host "5. NÃO marque 'Initialize with README'" -ForegroundColor White
Write-Host "6. Clique em 'Create repository'" -ForegroundColor White

Write-Host "`n⏳ Após criar o repositório, pressione ENTER para continuar..." -ForegroundColor Yellow
Read-Host

# Executar comandos Git
Write-Host "`n🔄 Executando comandos Git..." -ForegroundColor Yellow

Write-Host "🔄 Conectando com repositório GitHub..." -ForegroundColor Yellow
try {
    git remote remove origin 2>$null
    git remote add origin $repoUrl
    Write-Host "✅ Conectado com sucesso!" -ForegroundColor Green
} catch {
    Write-Host "❌ Erro ao conectar: $_" -ForegroundColor Red
    exit 1
}

Write-Host "🔄 Renomeando branch para main..." -ForegroundColor Yellow
try {
    git branch -M main
    Write-Host "✅ Branch renomeada!" -ForegroundColor Green
} catch {
    Write-Host "❌ Erro ao renomear branch: $_" -ForegroundColor Red
}

Write-Host "🔄 Fazendo push dos arquivos..." -ForegroundColor Yellow
try {
    git push -u origin main
    Write-Host "✅ Push realizado com sucesso!" -ForegroundColor Green
    Write-Host "`n🎉 SUCESSO! Repositório criado e configurado!" -ForegroundColor Green
    Write-Host "🔗 Acesse: https://github.com/$username/ufit-sales-agent" -ForegroundColor Cyan
    Write-Host "`n📁 Todos os arquivos estão agora no GitHub!" -ForegroundColor Green
} catch {
    Write-Host "❌ Erro ao fazer push: $_" -ForegroundColor Red
    Write-Host "`nTente executar manualmente:" -ForegroundColor Yellow
    Write-Host "   git push -u origin main" -ForegroundColor White
}

Write-Host "`nPressione qualquer tecla para sair..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
