from django.shortcuts import render



def home_handler(request):
    return render(request, 'home/home.html', {})