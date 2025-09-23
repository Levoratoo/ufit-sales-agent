#!/usr/bin/env python3
"""
Script para criar repositório no GitHub usando o novo token com permissões
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

    # Novo token com permissões (removido por segurança)
    token = "SEU_TOKEN_AQUI"

    # Verificar se estamos no diretório correto
    if not Path("main.py").exists():
        print("❌ Execute este script na pasta do projeto UFIT Sales Agent!")
        return False

    # Dados do repositório
    repo_data = {
        "name": "ufit-sales-agent",
        "description": "Agente de vendas inteligente para UFIT com sistema de aprovação automática e playbook de vendas consultivas",
        "private": False,
        "auto_init": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }

    # Headers para a API
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "UFIT-Sales-Agent"
    }

    print("🔄 Criando repositório no GitHub...")

    try:
        # Primeiro, verificar se o token funciona
        print("🔍 Verificando autenticação...")
        user_response = requests.get(
            "https://api.github.com/user", headers=headers)

        if user_response.status_code != 200:
            print(f"❌ Erro de autenticação: {user_response.status_code}")
            print(f"Resposta: {user_response.text}")
            return False

        user_info = user_response.json()
        print(f"✅ Autenticado como: {user_info['login']}")

        # Criar repositório
        print("🔄 Criando repositório...")
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

            # Verificar se já existe remote
            try:
                subprocess.run("git remote remove origin",
                               shell=True, check=False)
            except:
                pass

            # Adicionar remote
            subprocess.run(
                f"git remote add origin {clone_url}", shell=True, check=True)
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

        elif response.status_code == 422:
            print("⚠️ Repositório já existe! Tentando conectar...")
            # Tentar conectar com repositório existente
            repo_url = f"https://github.com/{user_info['login']}/ufit-sales-agent.git"

            try:
                subprocess.run("git remote remove origin",
                               shell=True, check=False)
                subprocess.run(
                    f"git remote add origin {repo_url}", shell=True, check=True)
                subprocess.run("git branch -M main", shell=True, check=True)
                subprocess.run("git push -u origin main",
                               shell=True, check=True)

                print(f"✅ Conectado com repositório existente!")
                print(
                    f"🔗 Acesse: https://github.com/{user_info['login']}/ufit-sales-agent")
                return True
            except subprocess.CalledProcessError as e:
                print(f"❌ Erro ao conectar: {e}")
                return False

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
            subprocess.run([sys.executable, "-m", "pip",
                           "install", "requests"], check=True)
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
