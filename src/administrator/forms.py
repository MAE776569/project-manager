from django import forms
from authentication.models import AccountVerification

class AddAccountVerificationForm(forms.ModelForm):
    class Meta:
        model = AccountVerification
        fields = ['name', 'email']
        help_texts = {
            'name': "Should be the real name of the user.",
            'email': "The email that will be used for verification and contact."
        }