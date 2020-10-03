from django import forms
from .models import account

class LoginForm(forms.ModelForm):

    class Meta:
        model = account
        fields = ('acct_no', 'pin')