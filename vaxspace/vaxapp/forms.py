from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Register, Vaccine, Barangay, Guardian
from django import forms





class CreateUserForm(UserCreationForm):
    barangay = forms.ModelChoiceField(queryset=Barangay.objects.all(), empty_label=None)
    contact = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2', 'barangay','contact']
         
