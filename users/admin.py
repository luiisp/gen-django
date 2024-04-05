from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import ProfileModel


class ProfileModelInline(admin.StackedInline):
    model = ProfileModel
    can_delete = False
    verbose_name_plural = "profile models"


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileModelInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)