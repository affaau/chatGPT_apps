:: To collect the rest of the text as one sentense
:: Ensure bat file is accessable in anywhere
:: e.g. copy to Windows directory
::
:: Issues: Encoutner error in classic command line window
@echo off
setlocal EnableDelayedExpansion
set "args="
set python_path=
for %%i in (%*) do (
    if defined args (
        set "args=!args! %%i"
    ) else (
        set "args=%%i"
    )
)
:: echo %args%

:: Pass to python script as input argument
:: include your full path of the script below
python D:\Workspace\Python\chatGPT\GPT_apps.py %args%
endlocal