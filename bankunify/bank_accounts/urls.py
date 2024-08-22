# bank_accounts/urls.py
from django.urls import path
from .views import BankAccountCreateView, BankAccountListView

urlpatterns = [
    path('add/', BankAccountCreateView.as_view(), name='bank-account-add'),
    path('', BankAccountListView.as_view(), name='bank-account-list'),
]
