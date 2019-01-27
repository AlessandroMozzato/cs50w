# Project 3

Web Programming with Python and JavaScript

The application was build in Django with HTML/CSS and Javascript for the front end.

I leveraged Django built in components for the login, which I only had to tweak in order to add the required fields like Name and Surname. Together with this component also came the relative dataset of users and the admin console, which I used to display orders from customers going into the order tab.

My app is composed of three main paged. A first page which prompt users to sign up or log in.
Once the user is logged in she is redirected to the main menu page. Here on the left are indicated all the elements on the menu. Clicking on these elements will add them on the cart on the right. For elements which have possible toppings I have added a drop down menu to add them to the order. 

Once the user has selected the elements she wants she can then confirm her order, which in turn will take her to the final order submission page. Here, after reviewing all the elements the user can submit the order. This will prompt the Stripe interface that allows the payment via credit card. This is my extra contribution. I used the stripe components directly from their website. This mainly consists of a javascript module which is called via a script tag. This module takes care of the credit cart input information and sends confirmations to the backend. 

In terms of tables I created for this project they are mainly 3.
The first table is the menu, it contains all the elements of the manu including name to display, price, size available, number and type of toppings that can be associated with the element. 
The second table is a table of carts, this table has a unique key for user id meaning every user can only have one cart at the time. This table contains all the content of the cart at every moment for every user.
The final table is the orders table. It contains the content of every order for every user.