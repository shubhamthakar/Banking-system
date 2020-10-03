from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class customer(models.Model):
    pan = models.CharField(max_length = 10,primary_key = True)
    #Pan regex can be added as input form validator or as database validator?
    fname = models.CharField(max_length = 15)
    mname = models.CharField(max_length = 15)
    lname = models.CharField(max_length = 15)
    date_birth = models.DateField()
    address1 = models.CharField(max_length = 40)
    address2 = models.CharField(max_length = 40)
    address3 = models.CharField(max_length = 40)

    def __str__(self):
        return self.fname 

class cust_phone(models.Model):
    customer = models.ForeignKey(customer, on_delete = models.CASCADE)
    phno = models.CharField(max_length = 10)

    def val_phone_no(self):
        return len(self.phno) == 10

    def __str__(self):
        return self.phno


class account(models.Model):
    acct_no = models.CharField(max_length = 13, primary_key = True)
    customer = models.ForeignKey(customer,default = "", on_delete = models.CASCADE)
    pin = models.PositiveSmallIntegerField()
    balance = models.DecimalField(max_digits = 12, decimal_places = 2)
    def has_money(self):
        return self.balance >= 0

    def __str__(self):
        return self.acct_no

class trans_info(models.Model):
    trans_id = models.AutoField(max_length = 12, primary_key = True)
    trans_date = models.DateTimeField()
    amount = models.DecimalField(max_digits = 12, decimal_places = 2)
    cred_acct_num = models.ForeignKey(account, on_delete = models.CASCADE, related_name = 'cred')
    deb_acct_num = models.ForeignKey(account, on_delete = models.CASCADE, related_name = 'deb')

    def __str__(self):
        return self.trans_id