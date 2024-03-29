# Patient Registration with API
- Django 4.0 based, 
- API included, DRF  Framework Used
- Slug and UUID
- URL Router
- CRUD Methodology with templates
- Class based View's
- Clean Code
- Login Account 
- ( In development progress ) 


Any sugesstions and ideas to improve or expand this aplication will welcome.


# Demo screens
![image](https://github.com/VoitecP/patient_registration/blob/5b578494de12197cf0abd03b09f89ddf1cbff94d/Demo%20images/Screen01.jpg)
![image](https://github.com/VoitecP/patient_registration/blob/5b578494de12197cf0abd03b09f89ddf1cbff94d/Demo%20images/Screen02.jpg)
![image](https://github.com/VoitecP/patient_registration/blob/5b578494de12197cf0abd03b09f89ddf1cbff94d/Demo%20images/Screen03.jpg)
![image](https://github.com/VoitecP/patient_registration/blob/5b578494de12197cf0abd03b09f89ddf1cbff94d/Demo%20images/Screen04.jpg)
![image](https://github.com/VoitecP/patient_registration/blob/5b578494de12197cf0abd03b09f89ddf1cbff94d/Demo%20images/Screen05.jpg)

## How To Setup
```
git clone https://github.com/VoitecP/patient_registration.git
```

Execude included Script BAT file:
- run-app-pip.bat  Will  create Virtual enviroment using pip and Run .
- run-app-pipen.bat (Recommended) will check if your local python instalation have package pipenv, then it will install, create Pipenv for that project and Run !

It will do all necessary work, install Virtual Env, with requirements, create .env file from template and run project !
But if you want to do it manually, just follow this steps:

```
cd patient_registration
```
Create Virtual Enviroment in Python and activate
```
py -m venv env
```
```
source env/bin/activate
```
```
pip install -r requirements.txt
```
You need to create  Enviroment file .env renaming env-template

Test database are already included !
```
py manage.py runserver
```
Project in Local Host server: http://127.0.0.1:8000/ 
