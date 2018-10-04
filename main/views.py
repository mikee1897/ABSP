from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, inlineformset_factory
from django.db.models import aggregates
from django.contrib import messages
import random

from main.models import Participant

from main.forms import ParticipantForm, Question1Form, Question2Form
# Create your views here.


def home(request):
    return render(request, 'main/home.html')

def personal_info(request):
    form = ParticipantForm(request.POST)
    participant = Participant.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main:question1')

    context = {
        'form' : form
    }

    return render(request, 'main/personal_info.html', context)

def question1(request):
    form = Question1Form(request.POST)
    participant_id = Participant.objects.latest('id')
    current_participant = Participant.objects.get(id=participant_id.id)
    value = random.randint(0,1)

    if (value == 0):
        language = participant_id.language1
    else:
        language = participant_id.language2

    if request.method == 'POST':
        if form.is_valid():
            current_participant.question1 = request.POST.get("question1")
            current_participant.save()
            return redirect('main:question2')

    context = {
        'form' : form,
        'language' : language
    }

    form.fields["question1"].initial = current_participant.question1

    return render(request, 'main/question1.html', context)

def question2(request):
    form = Question2Form(request.POST)
    participant_id = Participant.objects.latest('id')
    current_participant = Participant.objects.get(id=participant_id.id)
    value = random.randint(0,1)

    if (value == 0):
        language = participant_id.language1
    else:
        language = participant_id.language2

    if request.method == 'POST':  
        if form.is_valid():
            current_participant.question2 = request.POST.get("question2")
            current_participant.save()
            return redirect('main:end_page')

    context = {
        'form' : form,
        'language' : language
    }
    print(current_participant.question2)
 
    return render(request, 'main/question2.html', context)

def end_page(request):
    return render(request, 'main/end_page.html')