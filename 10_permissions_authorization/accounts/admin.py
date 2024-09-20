from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ]  # new
    fieldsets = UserAdmin.fieldsets + \
        (('Extra Details', {"fields": ("age", "address",
         "city", "zip", "state", "country", "phone")}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
        ((None, {"fields": ("age", "address", "city",
         "zip", "state", "country", "phone")}),)


admin.site.register(CustomUser, CustomUserAdmin)
