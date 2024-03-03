from django.shortcuts import render
from chat.models import Messages, Chat


json = {
    'username': "Kleme",
    'lastname': "Naue"
}

# "textmessage" ist der name des Inputfelds
def index(request):
    if request.method == "POST":
        print("Received Data " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Messages.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    return render(request, 'chat/index.html', json)