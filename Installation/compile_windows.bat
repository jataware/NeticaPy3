@ECHO OFF
CLS

REM Variables
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set ARCH=32bit || set ARCH=64bit
SET vcvarsall="C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Auxiliary\Build\vcvarsall.bat"

echo Checking requirements
call cython --version
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Cython not installed.
    echo Please install Cython, execute: pip install cython
    EXIT
)
if NOT EXIST %vcvarsall% (
    echo ERROR: Build Tools for Visual Studio 2017 not installed. 
    echo Please install them from https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017
    EXIT
)

echo Setup Build Tools for Visual Studio 2017.
call %vcvarsall% %PROCESSOR_ARCHITECTURE%

echo Compiling NeticaEx.o
IF %PROCESSOR_ARCHITECTURE% EQU x86  (copy Netica_API_504_windows\lib\32 bit\*.* Netica_API_504_windows\lib\) ELSE IF %PROCESSOR_ARCHITECTURE% EQU X86  (copy Netica_API_504_windows\lib\32bit\*.* Netica_API_504_windows\lib\) ElSE  (copy Netica_API_504_windows\lib\64bit\*.* Netica_API_504_windows\lib\)
cd Netica_API_504_windows\src
cl /c /I. NeticaEx.c /link ..\lib\Netica.lib
COPY *.obj ..\lib\
cd ..\..
copy Netica_API_504_windows\lib\Netica.dll
COPY Netica_API_504_windows\NeticaPy.pyx
for /f "tokens=*" %%a in ('python -c "import sysconfig; print(sysconfig.get_path('data'))"') do set PYDATA=%%a
SET PYINC="%PYDATA%\include"
SET PYLIBS="%PYDATA%\libs"
echo compiling cython to c
cython -a NeticaPy.pyx
cl  /nologo /LD /W4  /INetica_API_504_windows\src\ /I%PYINC%  /IC:\Python27\PC /FeNeticaPy.pyd  /TcNeticaPy.c    /link Netica_API_504_windows\lib\NeticaEx  /link Netica_API_504_windows\lib\Netica.lib /dll  /libpath:%PYLIBS% 
cl /LD /W4   /D_USRDLL /D_WINDLL  /INetica_API_504_windows\src\ /I%PYINC%  /IC:\Python27\PC  /TcNeticaPy.c    /link Netica_API_504_windows\lib\NeticaEx  /link Netica_API_504_windows\lib\\Netica.lib   /dll /libpath:%PYLIBS% /OUT:NeticaPy.dll

echo Cleaning up
del *.c
del *.html
del *.pyx
del *.obj
del *.lib
del Netica_API_504_windows\lib\Netica.dll
del Netica_API_504_windows\lib\Netica.lib
del Netica_API_504_windows\lib\NeticaEx.obj
del Netica_API_504_windows\src\NeticaEx.obj