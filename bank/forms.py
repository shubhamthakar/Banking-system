from django import forms
from .models import customer, account, trans_info, cust_phone

class NewCustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        labels = {'pan':'PAN Number',
                'fname':'First Name',
                'mname':'Middle Name',
                'lname':'Last Name',
                'date_birth':'Date of Birth',
                'address1':'Address Line 1',
                'address2':'Address Line 2',
                'address3':'Address Line 3'}
        widgets = {'date_birth':forms.SelectDateWidget(years = range(1900,2020))}

class AddAcctForm(forms.Form):
    pan = forms.CharField(label = 'PAN', max_length = 10)
    fname = forms.CharField(label = 'First Name')
    lname = forms.CharField(label = 'Last Name')

class PinForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ('pin',)
        widgets = {'pin' : forms.PasswordInput()}

class LoginForm(forms.ModelForm):

    class Meta:
        model = account
        fields = ('acct_no', 'pin',)
        widgets ={'pin':forms.PasswordInput()}

class TransactionForm(forms.Form):
    amt = forms.DecimalField(label = 'Amount', max_digits = 12, decimal_places = 2)
    credit_acct_no = forms.CharField(label = 'Credit Account Number', max_length = 13)
    pin = forms.CharField(label = 'Account Pin',max_length = 6, widget = forms.PasswordInput())

class addPh(forms.ModelForm):

    class Meta:
        model = cust_phone
        fields = ('phno',)