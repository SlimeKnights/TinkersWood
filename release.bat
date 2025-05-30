@echo off

IF EXIST build RMDIR /q /s build
IF EXIST "Tinker-Wood-#.#.#.jar" DEL "Tinker-Wood-#.#.#.jar"
MKDIR build

REM Copy required files into build directory
XCOPY src\main\resources build /s /i /q
XCOPY src\generated\assets build\assets /s /i /q

REM Zipping contents
cd build
REM TODO: locate version number from mods.toml
jar --create --file ../Tinker-Wood-#.#.#.jar *
cd ..

REM Removing build directory
RMDIR /q /s build
