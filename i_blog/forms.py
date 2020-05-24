from django import forms
from django.contrib.auth.models import User
from .models import Company, Extra



class InfoCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'validate'
        }
    ))
    tagline = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'materialize-textarea',
            'id':'textarea1'
        }
    ))
    link = forms.URLField(widget=forms.URLInput(
        attrs={
            'class':'validate'
        }
    ))
    website = forms.URLField(widget=forms.URLInput(
        attrs={
            'class':'validate'
        }
    ))
    perks = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'materialize-textarea',
            'id':'textarea2'
        }
    ))
    skills = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'materialize-textarea',
            'id':'textarea3'
        }
    ))


    status = forms.CharField(widget=forms.TextInput(
    ))


    class Meta:
        model = Company
        fields = ['name', 'link', 'website', 'tagline', 'perks', 'skills', 'resume', 'status']
