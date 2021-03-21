# django DIY mini blog
MDN tutorial
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog

## step
1. checkout

2. venv  
`cd <project path>`  
`python -m venv venv`  
`venv/Script/activate`  

3. install django  
(venv)  
`python -m pip install django==3.1.7`  
`python -m pip install --upgrade pip`  

4. database migrate   
`python manage.py makemigrations`  
`python manage.py migrate`  

5. run server  
`python manage.py runserver`  

6. setup data  
`python manage.py createsuperuser`  
http://~/admin/  
