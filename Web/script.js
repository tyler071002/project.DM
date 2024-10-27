const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

messageInput.addEventListener('input', () => {
    messageInput.style.height = 'auto';
    messageInput.style.height = messageInput.scrollHeight + 'px';
});

sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    if (message) {
        console.log("전송된 메시지:", message); // 여기에서 실제 전송 기능 구현
        messageInput.value = ''; // 메시지 입력창 초기화
        messageInput.style.height = 'auto'; // 높이 초기화
    }
});
