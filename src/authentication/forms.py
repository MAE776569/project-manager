from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model, password_validation
from django.core.validators import validate_email, RegexValidator
from django.utils.html import format_html

class LoginForm(AuthenticationForm):
    username = forms.EmailField(required=True, label="Email",
                validators=[validate_email])

    password = forms.CharField(
        label="Password",
        strip=True,
        widget=forms.PasswordInput
    )

    FIELD_NAME_MAPPING = {"username": "email"}
    def add_prefix(self, field_name):
        field_name = self.FIELD_NAME_MAPPING.get(field_name, field_name)
        return super().add_prefix(field_name)

def get_password_help_text():
    help_texts = password_validation.password_validators_help_texts()
    help_texts.append("""Password must contain at least one uppercase letter
        one lowercase letter, digit and special character.""")
    help_texts.append("The spaces at the start and the end will be trimmed.")
    help_items = [format_html('<li>{}</li>', help_text) for help_text in help_texts]
    return '<ul class="help-text-list">%s</ul>' % ''.join(help_items) if help_items else ''


class RegisterationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=True,
        widget=forms.PasswordInput,
        help_text=get_password_help_text(),
        validators=[
        RegexValidator(
            regex='^(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+*!=]).*$',
            message='''Password must contain at least
             one uppercase letter one lowercase letter, digit and special character.''',
            code='invalid_password'
        )]
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        strip=True,
        help_text="Enter the same password as before, for verification."
    )
    FIELD_NAME_MAPPING = {
        "username": "email",
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
