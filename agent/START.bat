@echo off
REM Professional Data Analytics Agent - Quick Start for Windows

echo.
echo ===================================================================
echo PROFESSIONAL DATA ANALYTICS AGENT - SETUP
echo ===================================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not installed!
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo OK: Python installed
echo.

REM Check and create virtual environment
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    echo OK: Virtual environment created
) else (
    echo OK: Virtual environment exists
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -q groq pandas numpy openpyxl

echo OK: Dependencies installed
echo.

REM Check for API key
if not defined GROQ_API_KEY (
    echo.
    echo ===================================================================
    echo IMPORTANT: Set your Groq API Key
    echo ===================================================================
    echo.
    echo 1. Get your API key from: https://console.groq.com
    echo 2. Run this command:
    echo.
    echo    set GROQ_API_KEY=your-api-key-here
    echo.
    echo Then run: python analytics_agent.py
    echo.
    pause
) else (
    echo OK: GROQ_API_KEY is set
    echo.
    echo ===================================================================
    echo READY TO START!
    echo ===================================================================
    echo.
    echo Starting Data Analytics Agent...
    echo.
    python analytics_agent.py
)
