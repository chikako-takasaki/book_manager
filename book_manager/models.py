import datetime
from django.db import models
from django.utils import timezone

GENDER_CHOICES = (
    (1, 'unborrowed'),
    (2, 'borrowed'),
)

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  publisher = models.CharField(max_length=200) 
  status = models.IntegerField(choices=GENDER_CHOICES)
  updated_at = models.DateTimeField(auto_now=True) 
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  def is_borrowed(self):
    if status == 1:
      return true
    else:
      return false

  def borrow_book(self):
    self.status = 2
    self.save()

  def return_book(self):
    self.status = 1
    self.save()

