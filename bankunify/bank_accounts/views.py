from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import BankAccount
from .forms import BankAccountForm

class BankAccountCreateView(LoginRequiredMixin, CreateView):
    model = BankAccount
    form_class = BankAccountForm
    template_name = "bank_accounts/bank_account_form.html"
    success_url = reverse_lazy('bank-account-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BankAccountListView(LoginRequiredMixin, ListView):
    model = BankAccount
    template_name = "bank_accounts/bank_account_list.html"

    def get_queryset(self):
        return BankAccount.objects.filter(user=self.request.user)

class BankAccountUpdateView(UpdateView):
    model = BankAccount
    form_class = BankAccountForm
    template_name = "bank_accounts/bank_account_form.html"
    success_url = reverse_lazy('bank-account-list')

    def form_valid(self, form):
        if form.cleaned_data['password']:
            form.instance.set_password(form.cleaned_data['password'])
        return super().form_valid(form)