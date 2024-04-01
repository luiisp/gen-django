from django.shortcuts import render, redirect
import re
from django.contrib.auth import login, get_user_model

main_page = "auth/sign_up.html"
next_page = "menu"


def get_sign_up(request):
    return render(request, main_page)

def post_sign_up(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    username = request.POST.get('username')
    password_confirm = request.POST.get('confirm_password')

    # fields validation
    if not email or not password or not username or not password_confirm:
        return render(request, main_page, {'error': 'Todos os campos devem ser preenchidos'})

    print(f"try to sign up with {email}/{username} and {password}")
    if password != password_confirm:
        return render(request, main_page, {'error': 'As senhas não correspondem'})

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return render(request, main_page, {'error': 'Endereço de email inválido'})

    if len(password) < 8 or len(password) > 20 or not re.search(r'\W', password):
        return render(request, main_page, {'error': 'A senha deve ter entre 8 e 20 caracteres e conter pelo menos um símbolo'})

    user = get_user_model().objects.create_user(email=email,username=username, password=password)
    login(request, user)
    return redirect(next_page)
    