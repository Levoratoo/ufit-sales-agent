#!/usr/bin/env python3
"""
Script para fazer upload dos arquivos principais para o GitHub
"""

import subprocess
import sys
import os


def run_command(command):
    """Executa um comando e retorna o resultado"""
    try:
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def main():
    print("🚀 Iniciando upload para GitHub...")

    # Lista dos arquivos principais para upload
    files_to_upload = [
        "streamlit_database.py",
        "database/vendas_completo_unificado.json",
        "database/areas_config.json",
        ".cspell.json",
        "requirements.txt",
        "DATABASE_README.md"
    ]

    # Verificar se os arquivos existem
    missing_files = []
    for file in files_to_upload:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print(f"❌ Arquivos não encontrados: {missing_files}")
        return False

    # Adicionar todos os arquivos
    print("📁 Adicionando arquivos ao git...")
    success, stdout, stderr = run_command("git add .")
    if not success:
        print(f"❌ Erro ao adicionar arquivos: {stderr}")
        return False

    # Fazer commit
    print("💾 Fazendo commit...")
    success, stdout, stderr = run_command(
        'git commit -m "Atualização completa: nova interface de base de conhecimento"')
    if not success:
        print(f"❌ Erro ao fazer commit: {stderr}")
        return False

    # Fazer push
    print("⬆️ Fazendo push para GitHub...")
    success, stdout, stderr = run_command("git push origin main")
    if not success:
        print(f"❌ Erro ao fazer push: {stderr}")
        return False

    print("✅ Upload concluído com sucesso!")
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
