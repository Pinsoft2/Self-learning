# ✨ JJNoFish ✨

#### Video Demo:  <URL HERE>

## Description:
This is an app that allows users to replace word with another word inside of a word doc. Currently there is no limit on the number of word pairs within the app. Users are also able to track their histories of uploads through History tab.

## Origin / Background Story

JJ No Fish orgininated from my own phobic against fish due to a childhood trauma. This aims to be a prototype for a tool that works as a filter-of-all, the ideal version would work not just with word docs within a webapp, but all types of files, graphics and videos on a browser, a device or even embedded within an OS directly.

> For this project itself, it serves as my first experiment for replacing words that trigger bad experience with words that are more acceptable. It is an app that definitely owns its uniqueness against all the projects I have completed with CS50, even all my online projects so far. It's not an email service, not a network app and definitely not an auction app 😜


## Contents

+ Folders:

1. jjnofish

- models.py
Creates and defines the 2 most important classes for data storage - User and Uploadeddocument.

- project.py
Contains all of the main function of JJ No Fish.
- views.py
Contains all views for history, main function, login/out/create account.

2. templates
Contains all HMTL required for the web app.

3. static
- index.js
This JS file is in charge of all front end activities.

- style.css
In charge of all styling on the webapp.

4. Documents
This folder receives all files being sucessfully uploaded to the server in order to process the data. As a private app we keep these documents for the purpose of proj Capstone, but in the future we look to store these in cloud for data secuirity and load consideration.

5. modified_documents
This folder stores all modified documents and will revert back to user through Export function.


## Getting Started

1. Download the distribution code and unzip it.
2. In your terminal, cd into the <code>Capstone</code> directory.
3. Run <code>python manage.py makemigrations capstone</code> to make migrations for the network app.
4. Run <code>python manage.py migrate</code>  to apply migrations to your database.