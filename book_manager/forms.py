from django import forms
from django.contrib.auth.forms import AuthenticationForm 
 
from .models import Book

class BookForm(forms.ModelForm):
  
  class Meta:
    model = Book
    fields = ("title", "author", "publisher", "image_url")

    widgets = {
      'title': forms.TextInput(attrs={'size': 200}),
      'author': forms.TextInput(attrs={'size': 200}),
      'publisher': forms.TextInput(attrs={'size': 200}),
      'image_url': forms.TextInput(attrs={'size': 200}),
    }

class LoginForm(AuthenticationForm):
  
  def __init__(self, *args, **kwargs):
    super(LoginForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'
      field.widget.attrs['placeholder'] = field.label
          
