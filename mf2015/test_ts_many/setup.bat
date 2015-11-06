@echo off
REM The arguments for makewells.bat are:
REM   mode -- either "inject" or "pump"
REM   startrow
REM   endrow
REM   startcol
REM   endcol
REM
REM   startrow, endrow, startcol, and endcol define a well field rectangle,
REM   within which a well Q is assigned for each cell.
REM
REM   If mode = inject, Q is 10000.
REM      mode = pump, Q is -10000.
REM   makewells.bat can be edited to change Q values.

call makewells inject 101 150 101 150
call makewells pump 101 150 101 150
