from django import forms
from .models import projects


#Raw HTML form code with the modelform code (overwriting the original model)
class ProjectForm(forms.Form):
    project = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "Project Name", "class": "form-control"}))
    description = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "Project Name", "class": "form-control"}))
    created = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"placeholder": "Project Name", "class": "form-control"}))
    modified = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"placeholder": "Project Name", "class": "form-control"}))
    user = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"placeholder": "Project Name", "class": "form-control"}))
    status      = forms.CharField (required=False,widget=forms.TextInput(
        attrs={"placeholder": "Project Name", "class": "form-control"}))
	
class Meta:
    model = projects
    fields = [
        'project',
        'description',
        'created',
        'modified',
        'user',
        'status',
    ]


