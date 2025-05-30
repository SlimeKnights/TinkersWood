@echo off

REM setup run directory
mkdir run
mkdir run\mods

REM create dummy jar file with just meta-inf
IF EXIST build RMDIR /q /s build
IF EXIST "run\mods\Tinker-Wood-Dummy.jar" DEL "run\mods\Tinker-Wood-Dummy.jar"
mkdir build
XCOPY src\main\META-INF build\META-INF /s /i /q
copy src\main\pack.mcmeta build
copy src\main\pack.png build
cd build
jar --create --file ../run/mods/Tinker-Wood-Dummy.jar *
cd ..
REM Removing build directory
RMDIR /q /s build

REM create symlinks so resources live update. Using Json Things for testing but its not needed at runtime.
mkdir run\thingpacks
cd run\thingpacks
IF NOT EXIST TinkersWood mklink /J TinkersWood ..\..\src
IF NOT EXIST TinkersWoodGenerated mklink /J TinkersWoodGenerated ..\..\generated
cd ..\..