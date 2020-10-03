from django.shortcuts import render, get_object_or_404
from .models import account
from django.utils import timezone
from .forms import LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        acct_no = request.POST.get('acct_no')
        pin = request.POST.get('pin')
        user = account.objects.filter(acct_no=acct_no, pin=pin).first()
        print(user)
        if user is not None:
            return redirect('acct_details', acct_no=acct_no)
        else:
            messages.info(request, '* Account No.(12 digit) or Pin(6 digit) is incorrect')
            return redirect('login_page')
    form = LoginForm()
    return render(request, 'bank/login_page.html', {'form':form})

def acct_details(request, acct_no):
    acct = account.objects.get(acct_no=acct_no)
    return render(request, 'bank/acct_details.html', {'acct':acct})