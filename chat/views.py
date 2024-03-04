from django.shortcuts import render
from chat.models import Messages, Chat


json = {
    'username': "Kleme",
    'lastname': "Naue"
}

# request 
# "textmessage" ist der name des Inputfelds
# erstelle neue Message mit der Nachricht und den angegebenen Emfängern
def index(request):
    if request.method == "POST":
        print("Received Data " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Messages.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessage = Messages.objects.filter(chat__id = 1)
    return render(request, 'chat/index.html', {'messages' : chatMessage})