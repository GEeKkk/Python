@echo off
mode con lines=30 cols=60
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
:main
cls
color 1f

cls
color 1f
copy /y "hosts" "%SystemRoot%\System32\drivers\etc\hosts"
ipconfig /flushdns

echo.----------------------------------------
echo ���Ǳ���hosts+ˢ�±���DNS�����������!
echo.https://www.google.com/ncr
echo.https://www.google.com.hk/ncr
echo.----------------------------------------
goto end

:end
echo ��������˳�...
@Pause>nul