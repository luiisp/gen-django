from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .views_handler.home.home_handler import home_handler
from .views_handler.docs_about.docs_handler import docs_handler
from .views_handler.auth.sign_in_handler import get_sign_in,post_sign_in
from .views_handler.auth.sign_up_handler import get_sign_up,post_sign_up
from .views_handler.pages.menu_handler import menu_handler
from .utils.main import only_not_logged

# views manager


class Home(View):
    def dispatch(self, request, *args, **kwargs): # only user not looged
        return only_not_logged(request, next_page='menu') or super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return home_handler(request)
    
        
class Docs(View):
    def get(self, request):
        return docs_handler(request)
    

class SignUp(View):
    def dispatch(self, request, *args, **kwargs):
        return only_not_logged(request, next_page='menu') or super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return get_sign_up(request)
    
    def post(self, request):
        return post_sign_up(request)
    
    
class SignIn(View):
    def dispatch(self, request, *args, **kwargs):
        return only_not_logged(request, next_page='menu') or super().dispatch(request, *args, **kwargs)


    def get(self, request):
        return get_sign_in(request)
        
    def post(self, request):
        return post_sign_in(request)
    
class SignOut(LoginRequiredMixin,View):
    login_url = 'home'

    def post(self, request):
        return redirect('home')
    
class Menu(LoginRequiredMixin,View):
    login_url = 'home'
    
    def get(self, request):
        return menu_handler(request)