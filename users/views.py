from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.contrib.auth.decorators import login_required


# Create your views here.


class RegisterView(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form':form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('form valid')
            form.save()
            return redirect('user_login')
        print('form invalid')
        return render(request, 'users/register.html', {'form':form})



class ProfileView(LoginRequiredMixin,UserPassesTestMixin , DetailView):
    model = User

    def test_func(self):
        user = self.get_object()
        if user == self.request.user:
            return True
        return False



class UserProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, 'users/user_profile_update.html', {'u_form':u_form, 'p_form':p_form})

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            print(f'forms are valid')
            u_form.save()
            p_form.save()
            return redirect('user_profile', request.user.id)
        print(f'forms not valid')
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, 'users/user_profile_update.html', {'u_form':u_form, 'p_form':p_form})

        


            
