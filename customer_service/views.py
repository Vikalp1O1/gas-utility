
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ServiceRequestForm
from .forms import LoginForm
from .models import ServiceRequest, CustomerProfile

# Home Page (Dashboard)
def home(request):
    return render(request, 'customer_service/home.html')

# User Registration
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'customer_service/signup.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect after successful login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'customer_service/login.html', {'form': form})
# User Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Service Request Creation (for logged-in users)
@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/create_request.html', {'form': form})

# List Service Requests (for customers to track requests)
@login_required
def service_request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customer_service/service_request_list.html', {'requests': requests})

