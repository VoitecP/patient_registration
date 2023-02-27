@Echo Off

Set "PROJECT_DIR=patient_registration"
Set "VIRTUAL_ENV=env"

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    pip.exe install virtualenv
    python.exe -m venv %VIRTUAL_ENV%
)

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" Exit /B 1

Call "%VIRTUAL_ENV%\Scripts\activate.bat"

:: Project folder path
cd /d  %~dp0%PROJECT_DIR%\

:: Copying .env file from template
If Not Exist ".\.env" (
    echo f | xcopy /f /y .\env-template .\.env 
)    

pip.exe install -r requirements.txt

::@py.exe
::python manage.py cmd_fixtures
::@py.exe
python manage.py runserver

Pause
Exit /B 0


