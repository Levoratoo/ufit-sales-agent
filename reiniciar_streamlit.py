import subprocess
import sys
import time
import os


def reiniciar_streamlit():
    """Reinicia o Streamlit com auto-reload habilitado"""

    print("🔄 Reiniciando Streamlit...")

    # Matar processos Python existentes
    try:
        subprocess.run(["taskkill", "/f", "/im", "python.exe"],
                       capture_output=True, check=False)
        print("✅ Processos Python finalizados")
    except:
        print("⚠️ Nenhum processo Python encontrado")

    # Aguardar um momento
    time.sleep(2)

    # Iniciar Streamlit com auto-reload
    print("🚀 Iniciando Streamlit com auto-reload...")

    try:
        # Comando para iniciar Streamlit com auto-reload
        cmd = [
            sys.executable, "-m", "streamlit", "run",
            "streamlit_database.py",
            "--server.runOnSave", "true",
            "--server.fileWatcherType", "auto"
        ]

        # Iniciar em background
        process = subprocess.Popen(cmd,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        print("✅ Streamlit iniciado com sucesso!")
        print("🌐 Acesse: http://localhost:8502")
        print("📝 Auto-reload habilitado - mudanças nos arquivos serão detectadas automaticamente")
        print("\n💡 Dica: Agora quando você editar os arquivos JSON, o Streamlit recarregará automaticamente!")

        return process

    except Exception as e:
        print(f"❌ Erro ao iniciar Streamlit: {e}")
        return None


if __name__ == "__main__":
    reiniciar_streamlit()
