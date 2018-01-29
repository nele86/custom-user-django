from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.http import HttpResponse

from .forms import SignUpForm, LoginForm


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return render(request, 'account/register_done.html', {'user': user})
    else:
        form = SignUpForm()
    return render(request, 'account/sign_up.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # authenticate() checks users credentials and returns a user object
            user = authenticate(username=cd['email'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    # login() sets the user in current session
                    login(request, user)
                    return render(request, 'account/dashboard.html', {'user': user})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'account/login')
