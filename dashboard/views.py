from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages

@login_required
def dashboard(request):
    dashboard, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        # All fields for profile save/update
        dashboard.phone   = request.POST.get('phone', '')
        dashboard.address = request.POST.get('address', '')
        # add all keys you want editable 
        dashboard.save()
        # Username/email/password handled below, these are in User not UserProfile
        # Example username/email change:
        request.user.email = request.POST.get('email', request.user.email)
        request.user.save()
        # For password: 
        new_password = request.POST.get('password', '')
        if new_password:
            request.user.set_password(new_password)
            request.user.save()
        return redirect('profile')
    context = {
        'profile': profile,
        'user': request.user,
    }
    return render(request, 'dashboards/profile_page.html', context)


@login_required
def profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        # Update Django User model
        request.user.username = request.POST.get('username', request.user.username)
        request.user.email = request.POST.get('email', request.user.email)
        password = request.POST.get('password', '')
        if password:
            request.user.set_password(password)
        request.user.save()
        
        # Update UserProfile fields
        profile.phone = request.POST.get('phone', profile.phone)
        profile.address = request.POST.get('address', profile.address)
        profile.about = request.POST.get('about', profile.about)
        profile.save()

        messages.success(request, "Profile updated successfully!")
        
        from django.contrib.auth import update_session_auth_hash
        update_session_auth_hash(request, request.user)
        return redirect('profile')
    return render(request, 'dashboards/profile_page.html', {'user': request.user, 'profile': profile})

@login_required
def settings(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password:
            request.user.set_password(password)
            request.user.save()
            messages.success(request, "Password changed successfully!")
            # Optionally: Update session, re-login
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, request.user)

    
    return render(request, "dashboards/profile_page.html", {
        "user": request.user,
        "profile": UserProfile.objects.get_or_create(user=request.user)[0]
    })