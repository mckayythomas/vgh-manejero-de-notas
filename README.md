# vgh-manejero-de-notas

# Overview

This project was created as a proposed solution for the Colegio Victor Garcia Hoz. 
the base of the project is to create an API and database system to hold the colegio's grades of students
and to give their professors an easy way to update and add students grades.
The previous system introduced too many issues as it was just excel sheets held on a microsoft drive. 

This proposed solution involves a Django API web server that accesses a MySQL database. This project remains in the scope of local host but in a production environment would be ran using appropriate security measures and an .env file. 

A jquery front end also hosted in Django, is used for a user interface directly built to give professors and administrators an easy way to view student data. 

The file structure takes a modular approach separating the database items from the frontend items and from the API backend. This allows for large saleability and easy code restructure as needed. The SQL database is included in the file structure at the root and can be used to run the application as needed.

To start this web app you first need to download the SQL database. This can be found here:
[VGH Database](./VGH-Database-Backup.sql)

In MySQL workbench or the MySQL Shell, run the database file and make sure that the MySQL service is running on port 3306. If you don't have MySQL you can download it from here:
[MySQL Download](https://dev.mysql.com/downloads/workbench/)

Once the database is set up you can proceed to start the web application. 

We will first start a virtual environment and install all needed libraries. 

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements.txt
```

To view this web app you need to clone the repository and navigate to the vgh-django project folder with in. Once in the directory the following command line commands can be run:

```bash
cd vgh_django
python makemigrations
python migrate
python manage.py runserver
```


Once the server is running and you see a successful set up message one can navigate to the following urls to view the web app home page:
[http://127.0.0.1:8000/dashboard/profesor/](http://127.0.0.1:8000/dashboard/profesor/)
[http://127.0.0.1:8000/dashboard/tutor/](http://127.0.0.1:8000/dashboard/tutor/)
[http://127.0.0.1:8000/dashboard/director/](http://127.0.0.1:8000/dashboard/director/)

Each web page also has buttons in the nav bar to navigate between them.


[Django Web Page Demo Video](https://youtu.be/y7p1fFGeZ58)

# Web Pages

This Django app has 3 web pages in addition to the Django default admin center, and the REST Framework API call pages. The three main pages are the Profesor Dashboard, the Tutor Dashboard, and the Director Dashboard. Each of these pages uses dynamic JQuery to fill in table content for each individual to view their appropriate clases, estudiantes, tutoria, notas de estudiantes, and director niveles. In the future this application will allow many different profesores to access their unique information. Each profesor will be allowed to see each of their clases and respective students. 

# Development Environment

I used the Django framework to build this application. This application was designed as an API backend that communicates to a front end to retrieve and deliver data to the frontend. In order to build the API backend I used the Django REST Framework. Using this framework allowed me to easily build API endpoints and develop a functioning API. 
To build a front end I used Django templates in combination with Bootstrap 5 for styling and JQuery for dynamic web page and AJAX requests. 

# Useful Websites

* [Dev.io My personal Django rest framework serializer notes](https://dev.to/abdenasser/my-personal-django-rest-framework-serializer-notes-2i22)
* [Django REST Framework Documentation](https://www.django-rest-framework.org/)
* [How to Work with AJAX in Django](https://www.pluralsight.com/guides/work-with-ajax-django)
* [Django URL Template](https://www.askpython.com/django/django-url-template)
* [Modifying Serializer response in Django](https://forum.djangoproject.com/t/modifying-serializer-response-in-django-rest-framework/18993/5)
* [Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
* [Using Environment Variables in Django](https://codinggear.blog/django-environment-variables/)

# Future Work

* Add authentication and restrict routes - The whole idea behind this application is to allow users with certain auth levels to view their respective resources. By adding OAuth I can display the Profesor Dashboard to the appropriate profesores, the Tutoria Dashboard to those profesores who are tutors and in charge of a home room class, and finally the director Dashboard for those who are in charge of managing the different Nivel of students and profesor.  
* Add a more dynamic admin center - By using the Django default admin center it eliminates the need to make one myself. As of now the admin center is set up for viewing and changing all aspects of the database 
* Refactor and organize frontend code - I decided to try and follow Django conventions for templates and using javascript with in my templates. While this works great for being able to reuse HTML templates, having the Javascript nested into each HTML file is not as clean as I would like. I would prefer to take a more modular approach and create a static folder in my frontend application to store all of my JQuery and dynamic frontend code. This will give a cleaner file structure and help keep better track of business logic. 
* Add security measures - I would like to protect all routes and add better data validation.
* Unit Testing - Django offers what seems to be an easy and effective to use testing library. I had decided testing was out side of the scope of this project for the moment, but would prefer to create tests for each model, view, and serializer. 
* Add sessions - Sessions will be key in helping with auth but also holding user data for use with the webpages. As of now the AJAX routes are hard coded. By using sessions I can dynamically pass user information to API endpoints through AJAX to allow for a proper experience
* Add API documentation - Add in API endpoint documentation is key to having a well functioning app. This will also help will scaling the application as needed and as it grows. 
