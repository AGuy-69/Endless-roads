@echo off
rem Starts a local web server in this folder and opens Endless Road in your browser.
cd /d "%~dp0"
set PY=
where py >nul 2>nul && set PY=py -3
if "%PY%"=="" where python >nul 2>nul && set PY=python
if "%PY%"=="" (
  echo Python was not found. Install Python 3 from https://www.python.org/ and run this again.
  pause
  exit /b 1
)
%PY% serve.py %1
