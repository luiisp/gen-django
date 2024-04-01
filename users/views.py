
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views import View
from .views_handler.home.home_handler import home_handler
from .views_handler.docs_about.docs import docs_handler
import re

class Home(View):
    def get(self, request):
        return home_handler(request)
        
class Docs(View):
    def get(self, request):
        return docs_handler(request)
