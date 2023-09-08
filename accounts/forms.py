from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    video_file = forms.FileField(required=False) 
    profile_image = forms.ImageField(required=False)  # Keep the image field

    class Meta:
        model = CustomUser
        fields =  ("username",
                "profile_image",
                  "email",
                  "video_file",
                   "age",
                    "address" )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username",
                  "profile_image",
                  "video_file",
                  "email",
                   "age",
                    "address" )
