from django import forms
from django.forms import ModelForm, ValidationError, Form, widgets
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date, datetime
from django.forms.formsets import BaseFormSet

from main.models import Participant 

class DateInput(forms.DateInput):
    input_type = 'date'

class TermsForm(forms.ModelForm):
    
    class Meta:
        model = Participant
        fields = ('bilingual', 'data', 'authentic')

    bilingual = forms.BooleanField(widget = forms.CheckboxInput())
    data = forms.BooleanField(widget = forms.CheckboxInput())
    authentic = forms.BooleanField(widget = forms.CheckboxInput())

class LanguageForm(forms.ModelForm):
    LANGUAGE = (
        ('English', 'English'),
        ('Tagalog', 'Tagalog'),
        ('Korean', 'Korean'),
        ('Japanese', 'Japanese'),
        ('Mandarin', 'Mandarin'),
        ('Hokkien', 'Hokkien'),
        ('Cebuano', 'Cebuano'),
    )

    class Meta:
        model = Participant
        fields = ('first_language', 'second_language')

    first_language = forms.CharField(widget = forms.Select(choices=LANGUAGE))
    second_language = forms.CharField(widget = forms.Select(choices=LANGUAGE))

class NameForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('name',)

class IDForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('idnumber',)

class AgeForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('age',)
    
class GenderForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('gender',)

class CollegeForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('college',)

class EmailForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('email',)
   
class MobileForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('mobile',)

        widgets = {
            'mobile': forms.TextInput(attrs={'placeholder':'09xxxxxxxxx'})
        }
   
class InvestAmountForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('A_amount', 'B_amount')
        widgets = {
            'A_amount': forms.NumberInput(attrs={'name':'A_amount', 'id':'A_amount', 'max': '1000', 'maxlength': '5'}),
            'B_amount': forms.NumberInput(attrs={'name':'B_amount', 'id':'B_amount', 'readonly':'readonly'})
        }