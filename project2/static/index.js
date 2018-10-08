if (window.localStorage.hasOwnProperty("username") == false) {
    username = window.prompt("Your username","username");
    window.localStorage.setItem("username", username);
} else {
    username = window.localStorage.getItem("username");
}

function showUsername() {
    document.getElementById("username").innerHTML = username;
}

function showChatname() {
    if (window.localStorage.hasOwnProperty("chatname") == false) {
        document.getElementById("chatnamejs").innerHTML = "No chat selected";
    } else {
        chatname_txt = window.localStorage.getItem("chatname")
        document.getElementById("chatnamejs").innerHTML = chatname_txt;
    }
}

function storeChatname() {
    chatname_txt = document.getElementById("chatnameflask").innerHTML;
    window.localStorage.setItem("chatname", chatname_txt);
}

function showMessages() {
    const request = new XMLHttpRequest();
    request.open('POST', '/chatsapi');
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        console.log(chatname_txt)
        if (data[chatname_txt]) {
            arr = data[chatname_txt];
            for (var i = 0; i < arr.length; i++) {
                const li = document.createElement('li');
                li.innerHTML = arr[i];
                document.querySelector('#messages').append(li);
            }
        }
    }
    request.send();
};

document.addEventListener('DOMContentLoaded', () => {
    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    // When connected, configure buttons
    socket.on('connect', () => {
        // Each button should emit a "submit vote" event
        document.querySelector('#createchat').onclick = () => {
                var chatname = document.querySelector('#chatname').value;
                if (chatname == '') {
                    alert('Empty name is not allowed');
                } else {
                    socket.emit('create chat', {'chatname':chatname});
                }
        };

        document.querySelector('#newmessage').onclick = () => {
            var message = document.querySelector('#message').value;
            if (message == '') {
                alert('Empty messages are not allowed')
            } else {
                var d = new Date();
                date = d.getFullYear()+'-'+d.getMonth()+'-'+d.getDate()+' '+d.getHours()+':'+d.getMinutes()+':'+d.getSeconds();
                message = date + " " + username + " wrote: " + message + '::' + chatname_txt
                socket.emit('send message', {'message':message});
            }
        };
    });

    // When a new vote is announced, add to the unordered list
    socket.on('all chats', data => {
        if (data == 'Raise:error') {
            alert('Chatname already exists');
            document.querySelector('#chatname').value = '';
        } else {
        const li = document.createElement('li');
        li.innerHTML =  "<a href='/chats/"+data+"'>"+data+"</a></li>"; 
        document.querySelector('#chats').append(li);
        document.querySelector('#chatname').value = '';
        }
    });

    // When a new vote is announced, add to the unordered list
    socket.on('messages', data => {  
        const li = document.createElement('li');
        li.innerHTML =  data;
        document.querySelector('#messages').append(li);
        document.querySelector('#message').value = '';
    });
});
