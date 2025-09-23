#!/usr/bin/env python3
"""
Script para criar repositório no GitHub usando API
"""

import requests
import json
import subprocess
import sys
import os
from pathlib import Path

def criar_repositorio_github():
    """Cria repositório no GitHub usando API"""
    
    print("🚀 UFIT Sales Agent - Criação Automática do Repositório GitHub")
    print("=" * 60)
    
    # Verificar se estamos no diretório correto
    if not Path("main.py").exists():
        print("❌ Execute este script na pasta do projeto UFIT Sales Agent!")
        return False
    
    print("📋 Para criar o repositório automaticamente, você precisa de um Personal Access Token do GitHub.")
    print("\n🔑 COMO OBTER O TOKEN:")
    print("1. Acesse: https://github.com/settings/tokens")
    print("2. Clique em 'Generate new token' > 'Generate new token (classic)'")
    print("3. Dê um nome: 'UFIT Sales Agent'")
    print("4. Selecione as permissões:")
    print("   ✅ repo (Full control of private repositories)")
    print("   ✅ workflow (Update GitHub Action workflows)")
    print("5. Clique em 'Generate token'")
    print("6. COPIE o token (você só verá uma vez!)")
    
    token = input("\n🔑 Cole seu Personal Access Token aqui: ").strip()
    if not token:
        print("❌ Token é obrigatório!")
        return False
    
    # Dados do repositório
    repo_data = {
        "name": "ufit-sales-agent",
        "description": "Agente de vendas inteligente para UFIT com sistema de aprovação automática e playbook de vendas consultivas",
        "private": False,
        "auto_init": False
    }
    
    # Headers para a API
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    print("\n🔄 Criando repositório no GitHub...")
    
    try:
        # Criar repositório
        response = requests.post(
            "https://api.github.com/user/repos",
            headers=headers,
            data=json.dumps(repo_data)
        )
        
        if response.status_code == 201:
            print("✅ Repositório criado com sucesso!")
            repo_info = response.json()
            clone_url = repo_info["clone_url"]
            print(f"🔗 URL: {repo_info['html_url']}")
            
            # Configurar Git e fazer push
            print("\n🔄 Configurando Git e fazendo push...")
            
            # Adicionar remote
            subprocess.run(f"git remote add origin {clone_url}", shell=True, check=True)
            print("✅ Remote adicionado!")
            
            # Renomear branch
            subprocess.run("git branch -M main", shell=True, check=True)
            print("✅ Branch renomeada para main!")
            
            # Fazer push
            subprocess.run("git push -u origin main", shell=True, check=True)
            print("✅ Push realizado com sucesso!")
            
            print(f"\n🎉 SUCESSO! Repositório criado e configurado!")
            print(f"🔗 Acesse: {repo_info['html_url']}")
            print("📁 Todos os arquivos estão agora no GitHub!")
            
            return True
            
        else:
            print(f"❌ Erro ao criar repositório: {response.status_code}")
            print(f"Resposta: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar comando Git: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def main():
    try:
        # Verificar se requests está instalado
        try:
            import requests
        except ImportError:
            print("📦 Instalando biblioteca requests...")
            subprocess.run([sys.executable, "-m", "pip", "install", "requests"], check=True)
            import requests
        
        # Executar criação
        if criar_repositorio_github():
            print("\n✅ Processo concluído com sucesso!")
        else:
            print("\n❌ Falha no processo. Tente criar manualmente.")
            
    except KeyboardInterrupt:
        print("\n\n⏹️ Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
