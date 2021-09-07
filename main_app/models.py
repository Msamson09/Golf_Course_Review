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
  
  