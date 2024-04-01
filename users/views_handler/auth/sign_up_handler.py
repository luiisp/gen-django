from django.shortcuts import render
def sign_up_handler(request):
    return render(request, 'auth/sign_up.html')