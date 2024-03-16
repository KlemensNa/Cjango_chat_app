from django.http import HttpResponseRedirect
from django.shortcuts import render
from chat.models import Messages, Chat, userData
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
import json

# if user is not logged in, go to /login/
# request 
# "textmessage" ist der name des Inputfelds
# erstelle neue Message mit der Nachricht und den angegebenen Emfängern
@login_required(login_url="/login/")
def index(request):
    if request.method == "POST":
        print("Received Data " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        newMessage = Messages.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [ newMessage, ])
        returnedMessage = json.loads(serialized_obj[1:-1])
        print(returnedMessage)
        return JsonResponse(returnedMessage, safe=False)
    chatMessage = Messages.objects.filter(chat__id = 1)
    names = User.objects.all()
    return render(request, 'chat/index.html', {'messages' : chatMessage, 'userData': names })

    

def renderChatPartner():
    allUsers = User.objects.all()    
    return allUsers


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

def register(request):
    redirect = request.GET.get('next')
    if request.method == "POST":
        print("new Account registered: " + request.POST['registerName'] + '/brPassword: ' + request.POST['registerPassword'])
        user = User.objects.create_user(username=request.POST.get('registerName'),
                                 first_name=request.POST.get('Firstname'), 
                                 last_name=request.POST.get('Lastname'), 
                                 email=request.POST.get('registerEmail'),
                                 password=request.POST.get('registerPassword'))
        render(request, 'auth/login.html', {'redirect': redirect})
        # else:
        #     # boolean für if_Abfrage im login.html    
        #     # redirect as variable for the next url --> given to the hidden input
        #     return render(request, 'auth/register.html', {'accountAllreadyExists': True, 'redirect': redirect})
    return render(request, 'register/register.html', {'redirect': redirect})