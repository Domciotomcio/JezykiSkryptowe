@ECHO OFF

SET /A year= 2020
SET /A month= 10
SET /A day= 25
SET country=Poland

ECHO Dzien %day%.%month%.%year%, Kraj %country%
python zad2.py %year% %month% %day%
ECHO:
python zad3.py %country%
ECHO:
python zad4.py %year% %month% %day% %country%