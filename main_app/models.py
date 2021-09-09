from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField, IntegerField

# Create your models here.
class GolfCourse(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  hours_open = models.CharField(max_length=20)
  has_driving_range = BooleanField()
  price_9holes_wo_cart = IntegerField()
  price_9holes_w_cart = IntegerField()
  price_18holes_wo_cart = IntegerField()
  price_18holes_w_cart = IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # reviews = ManyToManyField(Review)

  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
      return reverse("golfcourse_detail", kwargs={"pk": self.pk})

class Photo(models.Model):
  url = models.CharField(max_length=250)
  golfcourse = models.OneToOneField(GolfCourse, on_delete=models.CASCADE)

  def __str__(self):
      return f"Photo for golfcourse_id: {self.golfcourse_id} @{self.url}"
  
  
  