from django import forms
from .models import projects


#Raw HTML form code with the modelform code (overwriting the original model)
class ProjectForm(forms.ModelForm):
    project     = forms.CharField (required=True)
    description = forms.CharField (required=True)
    created     = forms.CharField (required=False)
    modified    = forms.CharField (required=False)
    user        = forms.CharField (required=False)
    status      = forms.CharField (required=False)
	
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


