from django.shortcuts import render
def sign_in_handler(request):
    return render(request, 'auth/sign_in.html')