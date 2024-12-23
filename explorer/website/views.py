from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Your username or password was incorrect.")
            return redirect("home")

    return render(request, "home.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")

