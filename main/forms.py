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
        fields = ('speak', 'unidentifiable', 'imaginary')

    speak = forms.BooleanField(widget = forms.CheckboxInput())
    unidentifiable = forms.BooleanField(widget = forms.CheckboxInput())
    imaginary = forms.BooleanField(widget = forms.CheckboxInput())

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

    IDNUMBER = (
        ('112', '112'),
        ('113', '113'),
        ('114', '114'),
        ('115', '115'),
        ('116', '116'),
        ('117', '117'),
        ('118', '118'),
    )
    idnumber = forms.CharField(widget = forms.Select(choices=IDNUMBER))

class AgeForm(forms.ModelForm):
    age = forms.CharField(widget = forms.NumberInput(attrs={'name':'age', 'id':'age', 'type':'number'}))
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
    mobile = forms.CharField(widget = forms.NumberInput(attrs={'name':'mobile', 'id':'mobile', 'type':'number'}))
    class Meta:
        model = Participant
        fields = ('mobile',)

class InvestAmountForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('A_amount', 'B_amount')
        widgets = {
            'A_amount': forms.NumberInput(attrs={'name':'A_amount', 'id':'A_amount', 'max': '1000', 'maxlength': '5', 'type':'number'}),
            'B_amount': forms.NumberInput(attrs={'name':'B_amount', 'id':'B_amount', 'readonly':'readonly', 'type':'number'})
        }
        

class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('A_gain_loss', 'B_gain_loss')
        widgets = {
            'A_gain_loss': forms.NumberInput(attrs={'name':'A_gain_loss', 'id':'A_gain_loss', 'readonly':'readonly', 'type':'number'}),
            'B_gain_loss': forms.NumberInput(attrs={'name':'B_gain_loss', 'id':'B_gain_loss', 'readonly':'readonly', 'type':'number'})
        }