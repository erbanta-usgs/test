@echo off
if exist mf2015.nam del mf2015.nam
copy mf2015_str.nam mf2015.nam
..\..\mf2015\msvs\mf2015\debug\mf2015.exe
pause
