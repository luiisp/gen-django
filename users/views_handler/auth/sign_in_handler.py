from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

main_page = "auth/sign_in.html"
next_page = "home"


def get_sign_in(request):
    return render(request, main_page)

def post_sign_in(request):
    email_or_user = request.POST.get('email_or_user')
    password = request.POST.get('password')
    print(f"try to login with {email_or_user} and {password}")

    if not email_or_user or not password:
        return render(request, main_page, {'error': 'Todos os campos devem ser preenchidos'})

    if "@" in email_or_user:
        user = authenticate(request, email=email_or_user, password=password)
    else:
        user = authenticate(request, username=email_or_user, password=password)
        
    if user is not None:
        print("Login Ok")
        login(request, user)
        return redirect(next_page)
    else:
        print("Login Error")
        return render(request, main_page, {'error': 'Credenciais inválidas ou não cadastradas'})