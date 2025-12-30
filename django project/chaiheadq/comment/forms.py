from django import forms
from .models import comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class commentform(forms.modelform):
 class Meta:
    model = comment
    fields = ['text','photo']
    
class userregistrationform(UserCreationForm):
   email = forms.EmailField()
   class Meta:
      model = User
      fields = ('username','email','password1','password2')    