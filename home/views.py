from django.shortcuts import render, redirect

from .models import DareExchange

from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html")

# ======================================== DARES =================

def add_dare(request):
    if request.method == "POST":
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_phone_number = request.POST.get("phone_number")
        user_deadline = request.POST.get("deadline")
        user_dare = request.POST.get("dare")

        #Creating an object

        new_dare = DareExchange(
            name = user_name, 
            email =  user_email, 
            phone_number = user_phone_number,
            deadline = user_deadline,
            dare = user_dare
        )

        new_dare.save()

        print("new dare added successfully!")

        return redirect("dares")

    return render(request,"add_dare.html")

#  ==================================== CREATING DARE ==================

def dares(request):

    dares = DareExchange.objects.all()

    parameters = {
        "dares":dares
    }                   

    return render(request,"dares.html",parameters)

# =========================== DELETE A DARE =======================

def delete_dare(request,id):
    dare = DareExchange.objects.get(id = id)

    dare.delete()

    return redirect("dares")
# ============================= Edit A DARE ===========================


def edit_dare(request,id):
    dare = DareExchange.objects.get(id= id)

    if request.method == "POST":
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_phone_number = request.POST.get("phone_number")
        user_deadline = request.POST.get("deadline")
        user_dare = request.POST.get("dare")

        dare.name = user_name
        dare.email = user_email
        dare.phone_number = user_phone_number
        dare.deadline = user_deadline
        dare.dare = user_dare

        dare.is_edited = True

        dare.save()

        return redirect("dares")

    parameters = {
        "dare":dare
    }

   
    return render(request, "edit_dare.html", parameters)

# #  =================================
# # ======================== ACCOUNTS VIEWS ===========================
# from django.contrib import messages
# from django.contrib.auth.models import User
# from .models import UserProfile
# from django.contrib.auth import authenticate, login as auth_login

# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth.models import User
# from .models import UserProfile
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404


# # ======== Logout View =========
# def logout(request):
#     auth_logout(request)
#     return redirect('home')
# # ======== Profile View =========
# @login_required(login_url='login')
# def profile(request):
#     try:
#         user_profile = UserProfile.objects.get(user=request.user)
#     except ObjectDoesNotExist:
#         user_profile = None

#     context = {
#         'user_profile': user_profile
#     }
#     return render(request, 'accounts/profile.html', context)
# # ======== Login View =========
# def login(request):
#     if request.method == 'POST':
#         identifier = request.POST.get('identifier')  # Email or Phone
#         password = request.POST.get('password')

#         # Try to find the user by email first
#         try:
#             user_obj = User.objects.get(email=identifier)
#             username = user_obj.username
#         except User.DoesNotExist:
#             # If not found by email, try phone number
#             try:
#                 profile = UserProfile.objects.get(phone=identifier)
#                 username = profile.user.username
#             except UserProfile.DoesNotExist:
#                 username = None

#         if username:
#             # Authenticate the user
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 auth_login(request, user)  # Log the user in
#                 return redirect('home')  # Replace 'home' with your desired redirect target
#             else:
#                 messages.error(request, 'Invalid credentials. Please try again.')
#         else:
#             messages.error(request, 'User not found. Please check your identifier.')

#     return render(request, "accounts/login.html")
# #  ========= Register View =========
# def register(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         first_name = request.POST.get('firstName')
#         last_name = request.POST.get('lastName')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         college = request.POST.get('college')
#         year = request.POST.get('year')

#         # ✅ Remove phone from here (User model doesn't have this field)
#         new_user = User.objects.create(
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             is_staff=True  # ✅ This makes them visible in admin panel
#         )

#         new_user.set_password(password)
#         new_user.save()

#         # ✅ Store phone in UserProfile instead
#         UserProfile.objects.create(
#             user=new_user,
#             phone=phone,
#             college=college,
#             year=year
#         )

#         messages.success(request, 'Registration successful. You can now log in.')
#         return redirect('login')  # Redirect to login page after successful registration

#     return render(request, "accounts/register.html")
# # ======================== END OF ACCOUNTS VIEWS ===========================