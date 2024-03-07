from django.http import HttpResponseRedirect
from django.shortcuts import render
from chat.models import Messages, Chat
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# if user is not logged in, go to /login/
# request 
# "textmessage" ist der name des Inputfelds
# erstelle neue Message mit der Nachricht und den angegebenen Emfängern
@login_required(login_url="/login/")
def index(request):
    if request.method == "POST":
        print("Received Data " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Messages.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessage = Messages.objects.filter(chat__id = 1)
    return render(request, 'chat/index.html', {'messages' : chatMessage})


def indexLogin(request):
    # get "next" out of url e.g. url/next=/chat --> redirect = "/chat/"
    redirect = request.GET.get('next')
    if request.method == "POST":
        print("new Account logged in " + request.POST['loginName'] + ' mit dem Password ' + request.POST['loginPassword'])
        user = authenticate(username=request.POST.get('loginName'), password=request.POST.get('loginPassword'))
        if user: 
            login(request, user)
            if redirect:
                return HttpResponseRedirect(request.POST.get('redirect'))
            else:
                return  HttpResponseRedirect('/chat/')
        else:
            # boolean für if_Abfrage im login.html    
            # redirect as variable for the next url --> given to the hidden input
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})