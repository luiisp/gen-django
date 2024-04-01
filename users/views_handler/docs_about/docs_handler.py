from django.shortcuts import render

name = 'docs.html'
directory = 'docs_about'

def docs_handler(request):
    return render(request, f'{directory}/{name}', {})