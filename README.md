# feleves-feladat-tibcik

A féléves feladat egy betegnyilvántartó Django backend és Vue frontend megvalósítása.

### A projekt futtatásához szükséges:
 - Python 3.9.8
   - virtualenv 20.13.4
 - Node.js 16.14.0

### Installálás:
```
a Requirements.txt mappájában
> python.exe virtualenv web2_venv
> web2_venv/Scripts/activate
(web2_venv) > pip install -r requirements.txt

~web2_vue> npm intall
```

### Futtatás:
```
~web2_django> manage.py runserver
~web2_vue> npm run serve
```

- A backend a localhost:8000-as porton fut.
- A projekt a localhost:8080-as porton fut.
