## PROJECT QUESTIONNAIRE

**for Linux**

`git clone https://github.com/Amirshox/Questionnaire.git`

`cd Questionnaire`

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python3 manage.py migrate`

`python3 manage.py loaddata fixtures.json`

_login: `admin`_

_password: `1`_

`python3 manage.py runserver`