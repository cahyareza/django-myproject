# myprojects/apps/ideas/forms.py
from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
       model = Idea
       fields = "__all__"