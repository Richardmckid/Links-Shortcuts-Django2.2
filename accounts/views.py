from django.shortcuts import render, redirect
from django.contrib import auth, messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        # we now check if the user exists
        if user is not None:
            auth.login(request, user)
            print(user)
            return redirect('index')
        else:
            '''
            dont be specific for incase it is a malicious user 
            '''
            messages.error(request, 'Wrong credentials...')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out, please login...')
    return redirect('login')