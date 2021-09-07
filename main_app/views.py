from django.shortcuts import render, redirect
from .models import GolfCourse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

class GolfCourseList(ListView):
  model = GolfCourse

class GolfCourseCreate(CreateView):
  model = GolfCourse
  fields = '__all__'

class GolfCourseDetail(DetailView):
  model = GolfCourse

class GolfCourseUpdate(UpdateView):
  model = GolfCourse
  fields = [
    'hours_open',
    'price_9holes_wo_cart',
    'price_9holes_w_cart',
    'price_18holes_wo_cart',
    'price_18holes_w_cart'
  ]