from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.contrib import auth
from django.contrib.auth import logout



#  ========= Register View =========

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm = request.POST.get('confirmPassword')

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("create_account")
        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters.")
            return redirect("create_account")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please try a different one.")
            return redirect("create_account")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("create_account")
        
        from .models import UserProfile

        if UserProfile.objects.filter(phone=phone).exists():
            messages.error(request, "This Number already registered.")
            return redirect("create_account")



        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        UserProfile.objects.create(user=user, phone=phone)


        user.set_password(password)

        user.save()

        

        print("Account created successfully. Please log in.")
        return redirect("login")


    # GET request

    return render(request, 'account/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard") # profile url correct karo
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, 'account/login.html')  # correct path


def logout_request(request):
    logout(request)
    return redirect("login")
