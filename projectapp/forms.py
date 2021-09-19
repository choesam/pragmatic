from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
   class Meta:
       model = Project
       fields = ['image', 'title', 'description']