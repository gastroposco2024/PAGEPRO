from django import forms
from .models import Project, ProjectContact, Dish

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description','imagen']

class ProjectContact(forms.ModelForm):
    class Meta:
        model = ProjectContact 
        fields = ['name', 'email', 'message']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'image']