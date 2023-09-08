from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "profile_image",
        "username",
        "age",
        "video_file",
        "address",
        "is_staff",
    ]

    fieldsets =UserAdmin.fieldsets + ((None, {"fields": ("age","profile_image","address","video_file",)}), )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("age","profile_image","address","video_file",)}),)

admin.site.register(CustomUser, CustomUserAdmin)