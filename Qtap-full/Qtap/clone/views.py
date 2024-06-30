from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm, UserProfileForm
from .models import CustomUser
from .utils import generate_qr_code
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('edit_profile', nickname=user.nickname)
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('edit_profile', nickname=user.nickname)
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('login')

@login_required
def user_profile(request, nickname):
    user = get_object_or_404(CustomUser, nickname=nickname)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_view', nickname=user.nickname)
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'edit-profile.html', {'form': form, 'user': user})

@csrf_exempt
def generate_qr_code_view(request, nickname):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, nickname=nickname)
        qr_code_file = generate_qr_code(f'https://yourwebsite.com/profile/{user.nickname}')
        user.qr_code.save(f'{user.nickname}_qr_code.png', qr_code_file, save=True)
        return JsonResponse({'qr_code_url': user.qr_code.url})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def profile_view(request, nickname):
    user = get_object_or_404(CustomUser, nickname=nickname)
    return render(request, 'views-profile.html', {'user': user})
