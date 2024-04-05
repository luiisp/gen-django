from django.shortcuts import render
from ...models import ProfileModel

main_page = "my_account/profile.html"

def get_my_account(request):
    profile = ProfileModel.objects.get(user=request.user)
    return render(request, main_page, {'user': request.user, 'profile': profile})