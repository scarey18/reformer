from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .models import User


class UserCreate(CreateView):
	model = User
	fields = ['username', 'email', 'password']
	template_name = 'app/register.html'


class UserDetail(DetailView):
	model = User
	fields = ['username', 'email', 'password']