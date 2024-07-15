document.addEventListener('DOMContentLoaded', () => {
    var socket = io({
        transports: ['websocket']
    });

    var messagesList = document.getElementById('messages');
    var lastReceivedTime = null;

    socket.on('connect', function() {
        console.log('Connected to SocketIO server');
    });

    socket.on('after_connect', function(data) {
        console.log('Received after connect:', data);
    });

    socket.on('new_message', function(data) {
        console.log('Received new message:', data);

        var currentTime = new Date();
        var timeDiff = calculateTimeDifference(lastReceivedTime, currentTime);

        var newMessage = document.createElement('li');
        newMessage.textContent = `${data.message} ${timeDiff}`;
        messagesList.appendChild(newMessage);

        lastReceivedTime = currentTime;
    });

    function calculateTimeDifference(lastTime, currentTime) {
        if (lastTime) {
            var differenceInSeconds = Math.round((currentTime - lastTime) / 1000);
            return `(previous message: ${differenceInSeconds}s ago)`;
        } else {
            return '(first message since client refresh)'
        }
    }
});
