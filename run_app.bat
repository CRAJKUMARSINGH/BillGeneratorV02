@echo off
echo Starting Bill Generator App...
cd /d "%~dp0src"
streamlit run app.py
pause
