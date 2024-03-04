from django.shortcuts import render

def indexLogin(request):
    if request.method == "POST":
        print("new Account logged in " + request.POST['loginName'] + ' mit dem Password ' + request.POST['loginPassword'])
    return render(request, 'index.html')
