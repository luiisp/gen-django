from django.shortcuts import render

def docs_handler(request):
    return render(request, 'docs_about/docs.html', {})