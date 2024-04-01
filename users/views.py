from django.views import View
from .views_handler.home.home_handler import home_handler
from .views_handler.docs_about.docs import docs_handler
from .views_handler.auth.sign_in_handler import get_sign_in,post_sign_in
from .views_handler.auth.sign_up_handler import get_sign_up,post_sign_up

class Home(View):
    def get(self, request):
        return home_handler(request)
    
        
class Docs(View):
    def get(self, request):
        return docs_handler(request)
    

class SignUp(View):
    def get(self, request):
        return get_sign_up(request)
    
    def post(self, request):
        return post_sign_up(request)
    
    
class SignIn(View):
    def get(self, request):
        return get_sign_in(request)
        
    def post(self, request):
        return post_sign_in(request)