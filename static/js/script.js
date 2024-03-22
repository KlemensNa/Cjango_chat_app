async function sendMessage() {
    let fd = new FormData();
    let token = '{{csrf_token}}';
    let time = getDateInFormat();
    addFrontendMessage(messagetext.value);
    let backendMessage = messagetext.value;        
    fd.append("textmessage", messagetext.value);
    fd.append("csrfmiddlewaretoken", token);
    
    messagetext.value = "";
    try {
        await fetch('/chat/', {
            body: fd,
            method: "POST"
        })
        setTimeout(() => {
            document.getElementById("deleteMessage").remove();
            addBackendMessage(backendMessage);
        }, 1000)

        console.log("succesfully sended message", fd)
    } catch (e) {
        console.error("An error occured ", e)
    }
}

function addFrontendMessage(messagetext) {

    let date = getDateInFormat();
    messageContainer.innerHTML += `
    <div class="message row-reverse" id="deleteMessage">
        <div class="messageContainerImg"><img src="{% static '/img/avatarSofia.png' %}" alt=""></div>
        <div class="messageContainerMessage bubble-reverse">
            <div class="messageUsername">{{request.user.first_name}}</div>
            <div class="messageMessageTime">
                <div class="messageMessage">${messagetext}</div>
                <div class="messageTime">
                    ${date}
                    <div class="sendIcon"><img src="{% static '/img/check.svg' %}" alt=""></div>
                </div>
            </div>
        </div>            
    </div>
    `
}


function addBackendMessage(messagetext) {

    let date = getDateInFormat();
    messageContainer.innerHTML += `
    <div class="message row-reverse">
        <div class="messageContainerImg"><img src="{% static '/img/avatarSofia.png' %}" alt=""></div>
        <div class="messageContainerMessage bubble-reverse">
            <div class="messageUsername">{{request.user.first_name}}</div>
            <div class="messageMessageTime">
                <div class="messageMessage">${messagetext}</div>
                <div class="messageTime">
                    ${date}
                    <div class="sendIcon"><img src="{% static '/img/doublecheck.svg' %}" alt=""></div>
                </div>
            </div>
        </div>
        
    </div>
    `
}


function getDateInFormat() {
    let date = new Date();
    let month = date.getMonth();
    let day = date.getDate();
    let year = date.getFullYear();
    let hour = date.getHours()
    let minutes = date.getMinutes()
    let newDate = hour + ":" + minutes
    return newDate
}


function getMonthName(month) {
    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];

    return monthNames[month]
}

function checkText(){
    if(messagetext.value){
        messageButton.disabled = false
    } else {
        messageButton.disabled = true
    }
}

function toggleButton(){
        
    if(mypassword.value && myinput.value){
        sendButton.disabled = false
    } else {
        sendButton.disabled = true
    }
    
}