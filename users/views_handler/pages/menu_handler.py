from django.shortcuts import render

name = 'menu.html'
directory = 'pages'

def menu_handler(request):
    return render(request, f'{directory}/{name}', {})