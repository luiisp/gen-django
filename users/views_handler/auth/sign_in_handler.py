from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

main_page = "auth/sign_in.html"
next_page = "home"


def sign_in_handler(request):
    return render(request, main_page)

def make_login(request):
    email_or_user = request.POST.get('email_or_user')
    password = request.POST.get('password')
    if "@" in email_or_user:
        user = authenticate(request, email=email_or_user, password=password)
    else:
        user = authenticate(request, user=email_or_user, password=password)
        
    if user is not None:
        login(request, user)
        return redirect(next_page)
    else:
        return render(request, main_page, {'error': 'Credenciais inválidas ou não cadastradas'})