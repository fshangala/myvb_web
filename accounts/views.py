from django.shortcuts import render
from django.views.generic import FormView
from accounts.forms import RegisterForm, LoginForm

# Create your views here.
class RegisterView(FormView):
  template_name = 'accounts/register.html'
  form_class = RegisterForm
  redirect_authenticated_user = True
  success_url = '/'
  
class LoginView(FormView):
  template_name = 'accounts/login.html'
  form_class = LoginForm
  redirect_authenticated_user = True
  success_url = '/'