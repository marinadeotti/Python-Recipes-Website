# Recipes Website
#### **Video Demo:** https://youtu.be/uvO6oCFuMXk
#### **Description:** A website that allows the user to search for over 365,000 recipes and 86,000 food products.
#### **Technologies used:** Python, Flask, HTML, CSS, Jinja and Spoonacular API.
Developed by Marina Deotti for Harvard's CS50 course.

## About

This project was created exclusively for the conclusion of the "CS50 - Introduction to Computer Science" on-line course. I made the choice of building a Recipes website because cooking is something that I enjoy, and learning new tools while developing it was very inspiring. I kept the features simple yet functional. Even though it's a minimalistic website, I wanted it to feel and look inviting to the user. The color palette was carefully selected to reflect a website related to food.

## Project Structure

    static
        - css
        -- style.css
        - images
    templates
        - base.html
        - recipe.html
        - recipes.html
        - search.html
    setup.py

## What each file does

#### **`- static/css/style.css:`** contais all the CSS stylesheets for controling the appearance of the pages.
#### **`- templates/base.html:`** Jinja base template that extends the other pages of the website. Contains the calls for all the sylesheets and required JavaScripts for functionalities.
#### **`- templates/recipe.html:`** Recipe details page. Shows the summary, ingredients list, instructions and information about the recipe. The information is gathered from Spoonacular API.
#### **`- templates/recipes.html:`** Results page for the search made on the home page. Displays a list of recipes and the "See instructions" button bellow each result.
#### **`- templates/search.html:`** Homepage of the website, that contains the search forms. It's separated in three tabs: search by Recipe, search by Ingredients list and search by Nutrients.
#### **`- setup.py:`** creates global variables for the endpoints, routes homepage with the search.html template, contains the API headers for validating, routes each search form for the correct results, and collects details about each recipe.