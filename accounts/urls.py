from django.urls import path
from accounts.views import RegisterView
from accounts.views import LoginView
from django.contrib.auth.views import LogoutView

app_name="accounts"
urlpatterns = [
  path("register/", RegisterView.as_view(), name="register"),
  path("login/", LoginView.as_view(), name="login"),
  path("logout/", LogoutView.as_view(), name="logout"),
]