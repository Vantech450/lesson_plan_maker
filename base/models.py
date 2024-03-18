from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.
class SOW(models.Model):
  sow_id = models.IntegerField(primary_key=True, default=0)
  contents = ArrayField(models.TextField(blank=True), default=list, blank=True)
  
  def __str__(self):
    return str(self.sow_id)
  

class Save_Lesson(models.Model):
  name_id = models.ForeignKey(User, on_delete=models.CASCADE)
  contents = ArrayField(models.TextField(blank=True), default=list, blank=True)
  def __str__(self):
    return str(self.name_id)
