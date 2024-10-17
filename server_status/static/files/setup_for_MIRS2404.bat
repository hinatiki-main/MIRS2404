@echo off

winget install --id Cloudflare.cloudflared

echo Host mirs2404-pi-ssh > "%USERPROFILE%\.ssh\config"
echo    HostName mirs2404-pi-ssh.okakabase.net >> "%USERPROFILE%\.ssh\config"
echo    ProxyCommand cloudflared access ssh --hostname %%h >> "%USERPROFILE%\.ssh\config"

echo Host jetson-ssh >> "%USERPROFILE%\.ssh\config"
echo    HostName jetson-ssh.okakabase.net >> "%USERPROFILE%\.ssh\config"
echo    ProxyCommand cloudflared access ssh --hostname %%h >> "%USERPROFILE%\.ssh\config"

echo Setup complete! Press Enter to close.
pause >nul