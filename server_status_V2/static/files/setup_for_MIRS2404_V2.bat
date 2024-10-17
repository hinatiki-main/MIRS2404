@echo off
echo Downloading and installing the latest version of FortiClient...

REM Create a temporary folder
set TEMP_DIR=%TEMP%\FortiClient
mkdir %TEMP_DIR%

REM URL for the latest version of FortiClient
set URL=https://download-forticlient.okakabase.net/download/FortiClientVPNOnlineInstaller.exe

REM Download the file using PowerShell
echo Downloading FortiClient installer...
powershell -Command "Invoke-WebRequest -Uri %URL% -OutFile %TEMP_DIR%\FortiClientInstaller.exe"

REM Check if the download was successful
if not exist %TEMP_DIR%\FortiClientInstaller.exe (
    echo Download failed. Please check the URL and try again.
    pause
    exit /b
)

REM Install the downloaded FortiClient installer
echo Installing FortiClient...
%TEMP_DIR%\FortiClientInstaller.exe /quiet /norestart

REM Check the installation result
if %ERRORLEVEL% neq 0 (
    echo Installation failed with error code %ERRORLEVEL%.
    pause
    exit /b %ERRORLEVEL%
)

REM Clean up temporary files
rmdir /s /q %TEMP_DIR%

echo Installation completed successfully!