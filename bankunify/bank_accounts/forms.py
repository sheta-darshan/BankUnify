# bankunify\bank_accounts\forms.py
from django import forms
from .models import BankAccount, BankName

class BankAccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    bank_name = forms.ModelChoiceField(queryset=BankName.objects.all(), empty_label=None)

    class Meta:
        model = BankAccount
        fields = ['bank_name', 'bank_id', 'password']  # Include bank_name and password

    def save(self, commit=True):
        account = super().save(commit=False)
        if self.cleaned_data.get('password'):
            account.set_password(self.cleaned_data['password'])  # Encrypt the password
        if commit:
            account.save()
        return account
