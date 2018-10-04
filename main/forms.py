from django import forms
from django.forms import ModelForm, ValidationError, Form, widgets
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date, datetime
from django.forms.formsets import BaseFormSet

from main.models import Participant 

class DateInput(forms.DateInput):
    input_type = 'date'

class ParticipantForm(ModelForm):
    LANGUAGE = (
        ('Filipino', 'Filipino'),
        ('English', 'English'),
        ('Hokkien', 'Hokkien'),
        ('Mandarin', 'Mandarin'),
        ('Korean', 'Korean'),
        ('Japanese', 'Japanese'),
        ('Bisaya/Cebuano', 'Bisaya/Cebuano'),
    )

    COLLEGE = (
        ('BAGCED', 'BAGCED'),
        ('CCS', 'CCS'),
        ('COL', 'COL'),
        ('CLA', 'CLA'),
        ('COS', 'COS'),
        ('GCOE', 'GCOE'),
        ('RVRCOB', 'RVRCOB'),
        ('SOE', 'SOE'),
    )

    class Meta:
        model = Participant
        fields = ('idnumber', 'last_name', 'first_name', 'email', 'birthday', 'college', 'degree', 'mobile', 'language1', 'language2' )

        widgets = {
            'idnumber': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'xxxxxxxxx', 'maxlength':8}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Last Name'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'First Name'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : '09xxxxxxx'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Email'}),
            'birthday': DateInput(attrs={'class': 'form-control', 'placeholder' : 'Birthday'}),
            'college': forms.Select(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Degree'}),
            'language1': forms.Select(attrs={'class': 'form-control'}),
            'language2': forms.Select(attrs={'class': 'form-control'})
        }
        
class Question1Form(ModelForm):
    class Meta:
        model = Participant
        fields = ('question1',)

        CHOICES = (
            ('A', 'A'),
            ('B', 'B'), 
        )

        widgets = {
            'question1': forms.Select(choices= CHOICES, attrs={'class': 'form-control'})
        }

class Question2Form(ModelForm):
    class Meta:
        model = Participant
        fields = ('question2',)

        widgets = {
            'question2': forms.NumberInput(attrs={'class': 'form-control', 'maxlength':3})
        }

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)   
            self.fields["question2"].initial = Participant.objects.latest('id').question2