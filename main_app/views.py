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

def golfcourse_detail(request, pk):
  golfcourse = GolfCourse.objects.get(id = pk)
  return render(request, 'golfcourse/golfcourse_detail.html', {'golfcourse': golfcourse})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('golfcourse_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)