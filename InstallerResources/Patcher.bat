@echo off
title Rectify Patcher v0.2
color 01
md C:\Windows\Rectify10\Program
md C:\Windows\Rectify10\Program\Colorizer
md C:\Windows\Rectify10\Program\MicaForEveryone
md C:\Windows\Rectify10\Resources
md C:\Windows\Rectify10\Resources\Wallpepers
md C:\Windows\Rectify10\Resources\Temp
echo Install AccentColorizer...
copy C:\Rectify10\InstallFiles\Program\AccentColorizer C:\Windows\Rectify10\Program\Colorizer
start C:\Windows\Rectify10\Program\Colorizer\AccentColorizer.exe
echo Install MicaForEveryone...
copy C:\Rectify10\InstallFiles\Program\MicaForEveryone C:\Windows\Rectify10\Program\MicaForEveryone
echo install context menu...
copy C:\Rectify10\InstallFiles\Program\Nilesoft\AcrylicMenus C:\Windows\Rectify10\Resources
start C:\Windows\Rectify10\Resources\AcrylicMenusLoader.exe
echo install wallpepers...
copy C:\Rectify10\InstallFiles\Rectified C:\Windows\Rectify10\Resources\Wallpepers
echo succes
shutdown -r 20