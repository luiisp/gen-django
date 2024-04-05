from django.shortcuts import render

main_page = "my_account/profile.html"

def get_my_account(request):
    return render(request, main_page, {'user': request.user})