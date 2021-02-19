from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, reverse, render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_teacher = True
    #     if commit:
    #         user.save()
    #     return user
