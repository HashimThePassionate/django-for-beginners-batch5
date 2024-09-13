from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Make sure to define the fields explicitly as a tuple or list
        fields = tuple(UserCreationForm.Meta.fields) if isinstance(UserCreationForm.Meta.fields, (list, tuple)) else ('username', 'password1', 'password2')  # Add default fields here
        fields += ('age', 'address', 'city', 'zip', 'state', 'country', 'phone',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Make sure to define the fields explicitly as a tuple or list
        fields = tuple(UserChangeForm.Meta.fields) if isinstance(UserChangeForm.Meta.fields, (list, tuple)) else ('username', 'email')  # Add default fields here
        fields += ('age', 'address', 'city', 'zip', 'state', 'country', 'phone',)
