from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(
        request,
        'users/registration.html',
        {
            'form': form
        }
    )

@login_required
def profile(request):
    if request.method == 'POST':
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        profileImageForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)

        if profileImageForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileImageForm.save()

            messages.success(request, 'Ваш аккаунт был успешно обновлен!')
            return redirect('profile')

    else:
        updateUserForm = UserUpdateForm(instance=request.user)
        profileImageForm = ProfileImageForm(instance=request.user.profile)

    data = {
        'updateUserForm': updateUserForm,
        'profileImageForm': profileImageForm
    }

    return render(request, 'users/profile.html', data)