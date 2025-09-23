#!/usr/bin/env python3
"""
Script para criar automaticamente o repositório no GitHub
"""

import subprocess
import sys
import os
from pathlib import Path

def executar_comando(comando, descricao):
    """Executa um comando e mostra o resultado"""
    print(f"🔄 {descricao}...")
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f"✅ {descricao} - Sucesso!")
            if resultado.stdout:
                print(f"   Saída: {resultado.stdout.strip()}")
        else:
            print(f"❌ {descricao} - Erro!")
            print(f"   Erro: {resultado.stderr.strip()}")
            return False
        return True
    except Exception as e:
        print(f"❌ {descricao} - Exceção: {e}")
        return False

def verificar_git_config():
    """Verifica se o Git está configurado"""
    print("🔍 Verificando configuração do Git...")
    
    # Verificar user.name
    resultado = subprocess.run("git config user.name", shell=True, capture_output=True, text=True)
    if resultado.returncode != 0 or not resultado.stdout.strip():
        print("❌ Git user.name não configurado!")
        nome = input("Digite seu nome para o Git: ")
        executar_comando(f'git config --global user.name "{nome}"', "Configurando user.name")
    
    # Verificar user.email
    resultado = subprocess.run("git config user.email", shell=True, capture_output=True, text=True)
    if resultado.returncode != 0 or not resultado.stdout.strip():
        print("❌ Git user.email não configurado!")
        email = input("Digite seu email para o Git: ")
        executar_comando(f'git config --global user.email "{email}"', "Configurando user.email")
    
    print("✅ Configuração do Git verificada!")

def main():
    print("🚀 UFIT Sales Agent - Criação Automática do Repositório GitHub")
    print("=" * 60)
    
    # Verificar se estamos no diretório correto
    if not Path("main.py").exists():
        print("❌ Execute este script na pasta do projeto UFIT Sales Agent!")
        sys.exit(1)
    
    # Verificar configuração do Git
    verificar_git_config()
    
    # Obter username do GitHub
    username = input("\n📝 Digite seu username do GitHub: ").strip()
    if not username:
        print("❌ Username é obrigatório!")
        sys.exit(1)
    
    # URL do repositório
    repo_url = f"https://github.com/{username}/ufit-sales-agent.git"
    
    print(f"\n🎯 Criando repositório: {repo_url}")
    print("\n📋 INSTRUÇÕES:")
    print("1. Acesse: https://github.com/new")
    print("2. Nome do repositório: ufit-sales-agent")
    print("3. Descrição: Agente de vendas inteligente para UFIT com sistema de aprovação automática")
    print("4. Marque como Público")
    print("5. NÃO marque 'Initialize with README'")
    print("6. Clique em 'Create repository'")
    
    input("\n⏳ Pressione ENTER quando tiver criado o repositório no GitHub...")
    
    # Comandos para conectar e fazer push
    comandos = [
        (f'git remote add origin {repo_url}', "Conectando com repositório GitHub"),
        ('git branch -M main', "Renomeando branch para main"),
        ('git push -u origin main', "Fazendo push dos arquivos")
    ]
    
    print("\n🔄 Executando comandos...")
    for comando, descricao in comandos:
        if not executar_comando(comando, descricao):
            print(f"\n❌ Erro ao executar: {comando}")
            print("Tente executar manualmente:")
            print(f"   {comando}")
            break
    else:
        print("\n🎉 SUCESSO! Repositório criado e configurado!")
        print(f"🔗 Acesse: https://github.com/{username}/ufit-sales-agent")
        print("\n📁 Seus arquivos estão agora no GitHub!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️ Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("Execute os comandos manualmente seguindo as instruções.")
