from django import forms
from .models import account, trans_info

class LoginForm(forms.ModelForm):

    class Meta:
        model = account
        fields = ('acct_no', 'pin')

class TransactionForm(forms.ModelForm):

    class Meta:
        model = trans_info
        fields = ('amount', 'cred_acct_num')