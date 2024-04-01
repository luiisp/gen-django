
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views import View
from .views_handler.home.home_handler import home_handler
from .views_handler.docs_about.docs import docs_handler
from .views_handler.auth.sign_in_handler import sign_in_handler
from .views_handler.auth.sign_up_handler import sign_up_handler
import re

class Home(View):
    def get(self, request):
        return home_handler(request)
        
class Docs(View):
    def get(self, request):
        return docs_handler(request)
    
class SignUp(View):
    def get(self, request):
        return sign_up_handler(request)
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password != password_confirm:
            return render(request, 'users/sign_up.html', {'error': 'Passwords do not match'})
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return render(request, 'users/sign_up.html', {'error': 'Invalid email address'})
        user = get_user_model().objects.create_user(email=email, password=password)
        login(request, user)
        return redirect('home')
    
class SignIn(View):
    def get(self, request):
        return sign_in_handler(request)
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/sign_in.html', {'error': 'Invalid email or password'})
