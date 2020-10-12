from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page, name = "login_page"),
    path('<int:acct_no>/',views.acct_details, name= "acct_details"),
    path('create/',views.create,name='create'),
    path('add/',views.cust_add_acct, name = "cust_add_acct"),
    path('<str:pan>/',views.pinnumber,name='pin_number'),
    path('<int:acct_no>/add_ph/', views.add_ph, name="add_ph"),
    path('<int:acct_no>/statement/',views.acct_statement, name = "acct_statement"),
    path('', views.index, name="index"),
    
    
]