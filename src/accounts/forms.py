from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from authentication.forms import get_password_help_text
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        strip=True,
        widget=forms.PasswordInput
    )
    new_password1 = forms.CharField(
        label="New password",
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
    new_password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        strip=True,
        help_text="Enter the same password as before, for verification."
    )

    FIELD_NAME_MAPPING = {
        "old_password": "old-password",
        "new_password1": "new-password",
        "new_password2": "new-password-confirmation"
    }
    def add_prefix(self, field_name):
        field_name = self.FIELD_NAME_MAPPING.get(field_name, field_name)
        return super().add_prefix(field_name)

class ProfilePictureUploadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True 

    class Meta:
        model = get_user_model()
        fields = ("avatar",)