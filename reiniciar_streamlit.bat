@echo off
echo 🔄 Reiniciando Streamlit com auto-reload...
echo.

REM Matar processos Python
taskkill /f /im python.exe >nul 2>&1
echo ✅ Processos Python finalizados

REM Aguardar
timeout /t 2 /nobreak >nul

REM Iniciar Streamlit com auto-reload
echo 🚀 Iniciando Streamlit...
streamlit run streamlit_database.py --server.runOnSave true --server.fileWatcherType auto

pause

