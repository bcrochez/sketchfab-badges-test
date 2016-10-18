from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

# Create your views here.


def index(request):
    return render(request, 'sketchfab/index.html')


def login_view(request):
    if request.user.is_authenticated :
        return redirect('index')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        #else:
            # show error
    return render(request, 'sketchfab/login.html')


def logged_out(request):
    logout(request)
    return render(request, 'sketchfab/logout.html')
