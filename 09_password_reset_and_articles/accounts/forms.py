from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = tuple(UserCreationForm.Meta.fields) if isinstance(UserCreationForm.Meta.fields, (list, tuple)) else ('username', 'password1', 'password2')
        fields += ('age', 'address', 'city', 'zip', 'state', 'country', 'phone', 'first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Exclude the 'usable_password' field to prevent it from being rendered
        if 'usable_password' in self.fields:
            self.fields.pop('usable_password')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Make sure to define the fields explicitly as a tuple or list
        fields = tuple(UserChangeForm.Meta.fields) if isinstance(UserChangeForm.Meta.fields, (list, tuple)) else ('username', 'email')  # Add default fields here
        fields += ('age', 'address', 'city', 'zip', 'state', 'country', 'phone',)
