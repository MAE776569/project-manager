from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model, password_validation
from django.core.validators import validate_email

class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True, label="Email",
                validators=[validate_email])

    FIELD_NAME_MAPPING = {"username": "email"}
    def add_prefix(self, field_name):
        field_name = self.FIELD_NAME_MAPPING.get(field_name, field_name)
        return super().add_prefix(field_name)

class RegisterationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=True,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        strip=True,
        help_text="Enter the same password as before, for verification.",
    )
    FIELD_NAME_MAPPING = {
        "password1": "password",
        "password2": "confirm-password"
    }

    def add_prefix(self, field_name):
        field_name = self.FIELD_NAME_MAPPING.get(field_name, field_name)
        return super().add_prefix(field_name)
    
    class Meta:
        model = get_user_model()
        fields = ("email",)
        field_classes = {}
