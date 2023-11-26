from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import RegisterUserForm, ProfileChangeForm, UserChangeForm
from .models import CustomUser
from catalog.models import TestDrive


def profile(request):
    testdrive = TestDrive.objects.filter(user__username=request.user.username).order_by('test_date')
    customuser = CustomUser.objects.get(user=request.user)
    return render(request, 'user/profile.html', {'customuser': customuser, 'testdrive': testdrive})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def logout_user(request):
    logout(request)
    return redirect('login')


class ProfileUpdate(UpdateView):
    model = CustomUser
    template_name = 'user/profile_change.html'

    form_class = ProfileChangeForm


def change(request):
    if request.method == 'POST':
        profile_form = ProfileChangeForm(request.POST, request.FILES, instance=request.user.customuser)
        user_form = UserChangeForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileChangeForm(instance=request.user.customuser)
        user_form = UserChangeForm(instance=request.user)
    return render(request, 'user/profile_change.html', {'profile_form': profile_form, 'user_form': user_form})


