from django.shortcuts import render, redirect
from .models import GolfCourse, Photo
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-west-2.amazonaws.com/'
BUCKET = 'golf-course-review'

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

class GolfCourseList(LoginRequiredMixin, ListView):
  model = GolfCourse

@login_required
def add_photo(request, pk):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, golfcourse=pk)
      # Remove old photo if it exists
      golfcourse_photo = Photo.objects.filter(golfcourse=pk)
      if golfcourse_photo.first():
        golfcourse_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('golfcourse_detail', pk=pk)

class GolfCourseCreate(LoginRequiredMixin, CreateView):
  model = GolfCourse
  fields = '__all__'

class GolfCourseDetail(LoginRequiredMixin, DetailView):
  model = GolfCourse

class GolfCourseUpdate(LoginRequiredMixin, UpdateView):
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
