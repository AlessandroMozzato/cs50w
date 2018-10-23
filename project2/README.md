# Project 2 - Flack

Web Programming with Python and JavaScript

I build the Flack application in Flask, CSS, HTML and Javascript.

When opening the page for the first time the user is prompted with inserting a username, which is stored using LocalStorage. This local storage is then used when the user opens the page again to be immediately logged in.

Then page then appears divided in two main columns, the chat list on the left and the specific open chat on the right. At the beginning everything is empty. The user can then create a new cchat inserting the name. Using websocket this action is propagated in every open instance of Flack. The chat is also inizialized and saved in the backend. The chat appears on the list which leads the user to select the chat. The selected chat is also stored in local storage so that the user sees it when he opens the page again.

When a chat is selected the user can then send messages to the chat. Using websocket messages sent are also emitted to every Flack applications open. Messages are also saved in the backend so that when the application is opened again or the user selects different chats they can be opened.

My special feature is that the user can select a color for the messages sent. This color is also transitted to all the clients so every users sees the messages in the selected colors!
