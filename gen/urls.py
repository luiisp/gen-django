
from django.contrib import admin
from django.urls import path
from django.conf import settings
from users.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('docs/', Docs.as_view(), name='docs'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signin'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
