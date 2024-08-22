from django.urls import path
from .views import HomeView, SignUpView, ProfileView, ProfileUpdateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", HomeView.as_view(), name = "home"),
    path("profile/", ProfileView.as_view(), name = "profile" ),
    path("registration/signup/", SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
   
]
