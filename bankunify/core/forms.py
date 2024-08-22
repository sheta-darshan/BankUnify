from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class CustomUserChangeForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        help_text='Leave empty if you do not want to change the password.'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        help_text='Confirm the new password.'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        
        if password1:
            user.set_password(password1)
        
        if commit:
            user.save()
        return user