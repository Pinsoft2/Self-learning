# ✨ JJNoFish ✨

#### Video Demo:  <URL HERE>

## Overview:
JJNoFish is a unique application designed to alleviate discomfort caused by specific words or phrases. By allowing users to replace triggering terms with more acceptable alternatives, JJNoFish aims to create a more pleasant reading experience. Whether it’s overcoming childhood phobias or simply personalizing content, this app provides a customizable solution.

## Origin / Background Story

JJ No Fish orgininated from my own phobic against fish due to a childhood trauma. This aims to be a prototype for a tool that works as a filter-of-all, the ideal version would work not just with word docs within a webapp, but all types of files, graphics and videos on a browser, a device or even embedded within an OS directly.

> For this project itself, it serves as my first experiment for replacing words that trigger bad experience with words that are more acceptable. It is an app that definitely owns its uniqueness against all the projects I have completed with CS50, even all my online projects so far. It's not an email service, not a network app and definitely not an auction app 😜

## Key Features
Word Replacement: Users can upload word documents and specify word pairs for replacement. JJNoFish then processes the document, replacing the designated words with their alternatives.
Unlimited Word Pairs: Unlike other tools, JJNoFish doesn’t impose restrictions on the number of word pairs. Users can customize their experience by adding as many replacements as needed.
History Tracking: The app maintains a history of uploaded documents, making it easy for users to revisit and modify their replacements over time.


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
4. Run <code>python manage.py migrate</code> to apply migrations to your database.
5. Run <code>python manage.py runserver</code> to start the app in a browser. Chrome recommended.


JJNoFish empowers users to curate their content, turning potentially distressing words into more comfortable expressions. Whether it’s conquering fears or personalizing text, JJNoFish is a step toward a more tailored reading experience. 🐠🔍

And truly appreciate CS50 for the amazing teaching, project challenges and the opportunity to create something that can potentially be the beginning of something really useful for my and many others' lives!!