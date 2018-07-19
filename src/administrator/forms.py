from django import forms
from authentication.models import AccountVerification

class AddAccountVerificationForm(forms.ModelForm):
    class Meta:
        model = AccountVerification
        fields = ['name', 'email']
