# vgh-manejero-de-notas

# Overview

This project was created as a proposed solution for the Colegio Victor Garcia Hoz. 
the base of the project is to create an API and database system to hold the colegio's grades of students
and to give their professors an easy way to update and add students grades.
The previous system introduced too many issues as it was just excel sheets held on a microsoft drive. 

This proposed solution involves a django API web server that accesses a MySQL database. 
This project remains in the scope of local host but in a production enviornment would 
be ran using appropiate security measures and an .env file. 

A jquery front end also hosted in django, is used for a user interface directly built to 
give professors and administrators an easy way to view student data. 

The file structure takes a modular approach seperating the database items from the frontend items
and from the API backend. This allows for large scaleablilty and easy code restructure as needed

To view this web app you need to clone the repository and navigate to the 
vgh-django project folder with in. Once in the directory the following comandline
commands can be run:

python makemigrations
python migrate
python manage.py runserver

Once the server is runing and you see a successful set up message one can navigate to 
the folowing urls to view the web app home page. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

{Describe each of the web pages you created and how the web app transitions between each of them.  Also describe what is dynamically created on each page.}

# Development Environment

{Describe the tools that you used to develop the software}

{Describe the programming language that you used and any libraries.}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Dev.io My personal django rest framework serializer notes](https://dev.to/abdenasser/my-personal-django-rest-framework-serializer-notes-2i22)
* [Web Site Name](http://url.link.goes.here)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1
* Item 2
* Item 3
