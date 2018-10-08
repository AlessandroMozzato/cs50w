# Project 1

Web Programming with Python and JavaScript

For this project I created 3 tables. A table for the book information, a table for the users informations containing username, userid and passwords and one table for the reviews containing userid bookid and review.

For the login page I added a nav component requiring a bit of javascript, all handled automatically by bootstrap, adding the bootstrap.js component. This allows the login page to switch between login and sign up.

When a user gets to the app he registers and is redirected to a page confirming the registration with a link to the login/register page. Here he can login and then is redirected to the login and then search page.

At the bottom right of the page I added a logout button for all the pages wich sends the user back to the index page and resets the session['user_id'] variable.

After logging or signing up the user is redirected to a slightly different index page with a greeting and a link to the search page.

In the search page the user can search for books by title/isbn/author, all requireing just 3 characters to start a search. Search results a re displayed as an unordered list and each results contains a link to a book page. The book page contains 