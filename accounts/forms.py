from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import get_user_model
# from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ['email','username']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ['email','username']