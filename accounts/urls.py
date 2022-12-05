from django.urls import path
from accounts.views import signup, user_login, user_logout
from django.shortcuts import redirect


# def redirect_to_login(request):
#     return redirect("login")


urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path("", signup, name="signup1"),
    path("logout/", user_logout, name="logout"),
]
