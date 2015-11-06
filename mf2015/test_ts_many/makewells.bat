@echo off
REM run wellfield.py

if "5"=="" goto usage

set startrow=%2
set endrow=%3
set startcol=%4
set endcol=%5

if "%1"=="inject" goto inject
if "%1"=="pump" goto pump

echo Error: First argument must be "inject" or "pump"
goto end

:inject
set q=10000
goto makefiles

:pump
set q=-10000

:makefiles
python wellfield.py %startrow% %endrow% %startcol% %endcol% %q%
goto end

:usage
echo Usage: makewells startrow endrow startcol endcol Q

:end
