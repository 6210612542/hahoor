from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
import re


def index(request):
    return render(request, "dormitory/index.html")


def about(request):
    return render(request, "user/about.html")


def login(request):
    return render(request, "dormitory/index.html")


def register(request):
    # Check this view use when call register page or use when submit register form
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        # Check username is already taken
        if User.objects.filter(username=username).first():
            return render(request, "user/register.html", {"fail_username": "This username is already taken"})
        # Check the validity of a Password
        if (len(password) < 8):
            return render(request, "user/register.html", {"fail_password": "Password must have at least 8"})
        elif not re.search("[a-z]", password):
            return render(request, "user/register.html", {"fail_password": "Password must have at least 1 of a-z"})
        elif not re.search("[A-Z]", password):
            return render(request, "user/register.html", {"fail_password": "Password must have at least 1 of A-Z"})
        elif not re.search("[0-9]", password):
            return render(request, "user/register.html", {"fail_password": "Password must have at least 1 of 0-9"})
        # Check re-password is same as password
        if password != re_password:
            return render(request, "user/register.html", {"fail_re_password": "Invalid password confirm"})
        # Check email is already taken
        if User.objects.filter(email=email).first():
            return render(request, "user/register.html", {"fail_email": "This email is already taken"})
        # Add Object User
        add_user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
        add_user.set_password(password)
        add_user.save()
        return render(request, "dormitory/index.html")
    return render(request, "user/register.html")


def logout(request):
    logout(request)
    return render(request, "dormitory/index.html")
