from django.shortcuts import redirect


def only_not_logged(request, next_page):
    print(f"only_not_logged: {request.user.is_authenticated}")
    if request.user.is_authenticated:
        return redirect(next_page)
    return False
