from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from loans.models import LoanApplication


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")
        phone = request.POST.get("phone")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        UserProfile.objects.create(
            user=user,
            role=role,
            phone=phone
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "register.html")



def login_view(request):

    if request.method == "POST":

        username_or_email = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        # First try username
        user = authenticate(
            request,
            username=username_or_email,
            password=password
        )

        # If username authentication fails,
        # try finding the user by email
        if user is None:
            try:
                existing_user = User.objects.get(
                    email=username_or_email
                )

                user = authenticate(
                    request,
                    username=existing_user.username,
                    password=password
                )

            except User.DoesNotExist:
                user = None

        print("LOGIN USER:", user)
        if user is not None:

            login(request, user)

            try:
                profile = UserProfile.objects.get(user=user)

                if profile.role == "officer":
                    return redirect("officer_dashboard")

                return redirect("dashboard")

            except UserProfile.DoesNotExist:
                messages.error(
                    request,
                    "User profile not found. Please contact admin."
                )
                return redirect("login")
            
        print("LOGIN FAILED:", username_or_email)
        messages.error(
            request,
            "Invalid username/email or password."
        )

    return render(request, "login.html")



def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def dashboard(request):
    applications = LoanApplication.objects.filter(
        customer=request.user
    ).order_by('-created_at')

    stats = {
    'total': applications.count(),
    'pending': applications.filter(status='pending').count(),
    'under_review': applications.filter(status='review').count(),
    'approved': applications.filter(status='approved').count(),
    'rejected': applications.filter(status='rejected').count(),
}

    return render(
        request,
        "dashboard.html",
        {
            "stats": stats,
            "applications": applications[:5],
        }
    )


def officer_dashboard(request):

    return render(
        request,
        "officer_dashboard.html"
    )

def home_view(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    return render(
        request,
        "profile.html",
        {
            "user_profile": user_profile
        }
    )