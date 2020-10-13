from django.shortcuts import render, get_object_or_404
from .models import account, trans_info, customer, cust_phone
from django.utils import timezone
from .forms import LoginForm, TransactionForm, NewCustomerForm, PinForm, addPh, AddAcctForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import random


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        acct_no = request.POST.get('acct_no')
        pin = request.POST.get('pin')
        user = account.objects.filter(acct_no=acct_no, pin=pin).first()
        if user is not None:
            return redirect('acct_details', acct_no=acct_no)
        else:
            messages.info(request, "Account number(11 digits) or pin is incorect")

    form = LoginForm()
    return render(request, 'bank/login_page.html', {'form':form})

def acct_details(request, acct_no):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            amount  = int(request.POST.get('amt'))
            cred_acct_num = request.POST.get('credit_acct_no')
            pin = request.POST.get('pin')
            cred_acct = account.objects.filter(acct_no=cred_acct_num).first()
            deb_acct = account.objects.get(acct_no=acct_no)
            if cred_acct is not None:
                if cred_acct.acct_no == deb_acct.acct_no:
                    messages.info(request, '* Invalid account number')
                elif amount < 0:
                    messages.info(request, '* Invalid ammount')
                elif (int(pin.strip()) != int(deb_acct.pin)):
                    messages.info(request, '* Invalid Pin')
                elif deb_acct.balance >= amount:
                    deb_acct.balance = deb_acct.balance - amount
                    cred_acct.balance = cred_acct.balance + amount
                    deb_acct.save()
                    cred_acct.save()
                    trans_info.objects.create(trans_date = timezone.now(),amount = amount, cred_acct_num = cred_acct, deb_acct_num = deb_acct)
                    messages.success(request, '* Transaction successful')

                else:
                    messages.info(request, '* Insufficient Balance!')
            else:
                messages.info(request, '* Account does not exist')
        
        return redirect('acct_details', acct_no=deb_acct.acct_no)
    
    form = TransactionForm()
    acct = account.objects.get(acct_no=acct_no)
    return render(request, 'bank/acct_details.html', {'acct':acct, 'transForm':form})

def index(request):
    return render(request,'bank/index.html')

def create(request):

    form = NewCustomerForm()

    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('pin_number',pan=form.instance.pan)

        #else:
         #   messages.info(request,'Invalid Entry')
           # return redirect('create')

    return render(request,'bank/create_account.html',{'form':form})

def pinnumber(request,pan):

    balance = 0
    acct_no = random.randrange(64000000000,65000000000)
    old_cust = customer.objects.filter(pan = pan).first()
    all_acct = account.objects.filter(customer = old_cust)
    pin = random.randrange(100000,999999)
    t = account(acct_no=acct_no, customer=old_cust, pin=pin, balance=balance)
    t.save()
    return render(request,'bank/account_pin.html',{'acct_no':acct_no,'all_acct':all_acct, 'pin':pin})

def acct_statement(request, acct_no):
    user_acct = account.objects.get(acct_no=acct_no)
    q2 = trans_info.objects.filter(deb_acct_num = user_acct)
    q3 = trans_info.objects.filter(cred_acct_num = user_acct)
    q4 = (q2.union(q3))
    q1 = q4.order_by('-trans_date')
    return render(request,'bank/acct_statement.html',{'q1':q1,'user_acct':user_acct})


def add_ph(request, acct_no):

    form = addPh()
    if request.method == "POST":
        form = addPh(request.POST)
        if form.is_valid():
            phno = request.POST.get('phno')
            acc = account.objects.filter(acct_no=acct_no).first()
            cust = acc.customer
            cust_ph = cust_phone.objects.filter(customer=cust).filter(phno=phno).first()
            if cust_ph is None:
                cust_phone.objects.create(customer=cust, phno=phno)
                messages.info(request, "Number linked successfully")
                return redirect('add_ph', acct_no=acct_no)
            else:
                messages.info(request, "Number is already linked")
                return redirect('add_ph', acct_no=acct_no)          
        
    acc = account.objects.filter(acct_no=acct_no).first()
    cust = acc.customer
    cust_ph = cust_phone.objects.filter(customer=cust)
    return render(request, 'bank/add_ph.html', {'cust_ph':cust_ph, 'acct_no':acct_no, 'form':form})

def cust_add_acct(request):
    form1 = AddAcctForm()
    if request.method == 'POST':
        pan = request.POST.get('pan')
        old_cust = customer.objects.filter(pan = pan).first()
        if old_cust is not None:
            return redirect("pin_number",pan=pan)
        else:
            messages.info(request, '* No records found')
            return redirect('cust_add_acct')
    return render(request, 'bank/add_acct_new.html',{'form1':form1})