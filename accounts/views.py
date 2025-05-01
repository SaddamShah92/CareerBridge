from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# User Registration View
def registration(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save() # Signals will create the UserProfile

            login(request, user)
            messages.success(request, "You have registered successfully!")
            return redirect('job_list')  # We'll handle where to send them next
        else:
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = CustomUserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


# Login View
def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")

            try:
                role = user.userprofile.role.lower()
            except UserProfile.DoesNotExist:
                messages.error(request, "No profile associated with this user.")
                return redirect('custom_login')

            if role == 'user':
                return redirect('job_list')
            elif role == 'hr':
                return redirect('job_list')
            elif role == 'admin':
                return redirect('/admin')
            else:
                messages.error(request, "Invalid role assigned.")
                return redirect('custom_login')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('custom_login')

    return render(request, "accounts/custom_login.html")

# Logout
@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('custom_login')

# Role-based Redirect View
@login_required
def login_redirect_view(request):
    role = request.user.userprofile.role
    if role == 'hr':
        return redirect('job_list')
    elif role == 'user':
        return redirect('job_list')
    elif role == 'admin':
        return redirect('admin_dashboard')
    else:
        return redirect('custom_login')
