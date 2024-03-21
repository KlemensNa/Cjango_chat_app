import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from chat.models import Messages, Chat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
import json

 

@login_required(login_url="/login/")
def index(request):
    """_summary_
    if message was sent(method=POST)
     this view creates a new Message with the actual time, the respective chat
     and serializes the created Message to JSON and returns the JSON-object
    if first called returns index.html with all chatMessages which are stored
    """
    if request.method == "POST":
        myChat = Chat.objects.get(id=1)
        time = get_time()
        newMessage = Messages.objects.create(text=request.POST['textmessage'] ,chat=myChat, author=request.user, receiver=request.user, created_at = time)
        serialized_obj = serializers.serialize('json', [ newMessage, ])
        returnedMessage = json.loads(serialized_obj[1:-1])
        return JsonResponse(returnedMessage, safe=False)
    chatMessage = Messages.objects.filter(chat__id = 1)
    names = User.objects.all()
    return render(request, 'chat/index.html', {'messages' : chatMessage, 'userData': names })

    

def render_chatpartner():
    """_summary_
    get List of all signed users
    Returns:
        set of all userdata
    """
    allUsers = User.objects.all()  
    print(allUsers) 
    return allUsers


def index_login(request):
    
    """_summary_
    get "next" out of url e.g. url/next=/chat --> redirect = "/chat/"    
    
    proofs if user is authenticated and log user in if True
    and returns redirect page of the request or chat page
    if Authentification is False, rerender login with new Variable for wrong Data text
    
    Returns:
        redirected page(in this case also chat page), chat page or login page 
    """
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
            return render(request, 'auth/login.html', {'wrongPassword': True, 'Greeting' : True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect, 'Greeting' : True, 'SignIn' : False})


def register(request):
    """_summary_
    this view returns the register page when first called
    If method is POST, when the form is sended, a user becomes created and it renders login page

    Returns:
        login page or the register page with variables to influence HTML code
    """
    redirect = request.GET.get('next')
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST.get('registerName'),
                                 first_name=request.POST.get('Firstname'), 
                                 last_name=request.POST.get('Lastname'), 
                                 email=request.POST.get('registerEmail'),
                                 password=request.POST.get('registerPassword'))
        return render(request, 'auth/login.html', {'redirect': redirect})
    return render(request, 'register/register.html', {'redirect': redirect, 'Greeting' : False, 'SignIn' : True})



def logout_user(request):
    """_summary_
    view renders the logout page and gives a dictionary with variables which influence HTML-Code
    Returns:
        render HTML and some variables
    """
    logout(request)
    return render(request, 'logout/logout.html', {'Greeting' : False, 'SignIn' : False})



def get_time():
    """_summary_
    this function return the actual time in "%H:%M"-format
    Returns:
        _type_: string
    """
    date = datetime.datetime.now()
    time = str(date.hour) + ":" + str(date.minute)
    
    return time