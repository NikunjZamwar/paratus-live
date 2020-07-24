"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


app_name = "main"

urlpatterns = [
    path("",  views.home, name="home"),
    path("basics",  views.basics, name="basics"),
    path("taxes",  views.taxes, name="taxes"),
    path("credit",  views.credit, name="credit"),
    path("retirement",  views.retirement, name="retirement"),
    path("student",  views.student, name="student"),
    path("investment",  views.investment, name="investment"),
    path("stocks",  views.stocks, name="stocks"),
    path("property",  views.property, name="property"),
    path("bonds",  views.bonds, name="bonds"),
    path("forum",  views.forum, name="forum"),
    path("signup", views.SignupView.as_view(), name='signup'),
    path("logout", views.logout_user, name='logout'),
    path("login", views.LoginView.as_view(), name='login'),
]
