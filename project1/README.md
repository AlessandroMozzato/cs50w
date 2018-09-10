# Project 1

Web Programming with Python and JavaScript

For this project I created 3 tables. A table for the book information, a table for the users informations containing username, userid and passwords and one table for the reviews containing userid bookid and review.

For the login page I added a nav component requiring a bit of javascript, all handle automatically by bootstrap adding the bootstrap.js component. This allows the login page to switch between login and sign up.

At the bottom right of the page I added a logout button for all the pages wich sends the user back to the index page and resets the session['user_id'] variable.

After logging or signing up the user is redirected to a slightly different index page with a greeting and a link to the search page.