from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUserModel = get_user_model()

# from .models import CustomUserModel

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email','username','is_staff','is_superuser']

admin.site.register(CustomUserModel,CustomUserAdmin)