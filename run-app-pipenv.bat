@Echo Off

Set "PROJECT_DIR=patient_registration"

:: Check for Pipenv instalation in Local computer 
pipenv --version 2>NUL

if errorlevel 1 (
    :: Instaling pipenv package, stable release
    ::pip.exe install pipenv
    pip.exe install pipenv==2022.11.30
)

:: Project folder path
cd /d  %~dp0%PROJECT_DIR%\

:: Copying .env file from template
:: Installing Virtual Environment -> pipenv install

If Not Exist ".\.env" (
    echo f | xcopy /f /y .\env-template .\.env  &  pipenv install
)    


:: Dump also requirments
:: pipenv requirements > requirements.txt

:: Run Django commands

:: pipenv run python manage.py cmd_fixtures
pipenv run python manage.py runserver



pause
Exit /B 0




