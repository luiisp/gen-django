from django.shortcuts import render
from ...models import ProfileModel

main_page = "my_account/edit_profile.html"

def get_edit_my_account(request):
    profile = ProfileModel.objects.get(user=request.user)
    return render(request, main_page, {'user': request.user, 'profile': profile})

