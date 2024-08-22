from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy # signup view using Django's built-in UserCreationForm
from typing import Any
from .forms import CustomSignUpForm, CustomUserChangeForm


# Home view using TemplateView
class HomeView(TemplateView):
    template_name = "core/home.html"
    
# Profile view using TemplateView
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "core/profile.html"
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user 
        return context

# signup view using CreateView  
class SignUpView(CreateView):
    form_class = CustomSignUpForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "registration/profile_edit.html"
    success_url = reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        return self.request.user

        

    
        