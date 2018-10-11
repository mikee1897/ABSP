from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, inlineformset_factory
from django.db.models import aggregates
from django.contrib import messages
import random
from decimal import Decimal

from main.models import Participant
from main.forms import TermsForm, LanguageForm, NameForm, IDForm, AgeForm, GenderForm, CollegeForm
from main.forms import EmailForm, MobileForm, InvestAmountForm
# Create your views here.


def page1(request):
    form = TermsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponseRedirect('../page2')
           
    context = {
        'form': form,
    }
    return render(request, 'main/page1.html', context)

def page2(request):
    form = LanguageForm(request.POST)
    quad = ""
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data = Participant.objects.latest('id')
            #random language
            language = [data.first_language, data.second_language]
            res = random.choices(language)
            data.language_used = res[0]
            #quandrant identification
            if data.first_language == "English":
                quad = "S"
            elif data.first_language == "Tagalog":
                quad = "S"
            elif data.first_language == "Korean":
                quad = "S"
            else:
                quad = "W"

            if data.second_language == "English":
                quad += "S"
            elif data.second_language == "Tagalog":
                quad += "S"
            elif data.second_language == "Korean":
                quad += "S"
            else:
                quad += "W"

            data.quadrant = quad
            data.save()
            return HttpResponseRedirect('../page3')
           
    context = {
        'form': form,
    }
    return render(request, 'main/page2.html', context)

def page3(request):
    data = Participant.objects.latest('id')
    form = NameForm(request.POST)
    audio_3 = ""
    # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        audio_3 = "MND/MND3.m4a"
    elif data.language_used == "Hokkien":
        audio_3 = "HOK/HOK3.m4a"
    else:
        audio_3 = "CEB/CEB3.m4a"
    
    if request.method == 'POST':
        if form.is_valid():
            data.name = request.POST.get('name')
            data.save()
            return HttpResponseRedirect('../page4')
           
    context = {
        'form': form,
        'audio_3': audio_3 
    }
    return render(request, 'main/page3.html', context)


def page4(request):
    data = Participant.objects.latest('id')
    form = IDForm(request.POST)

    audio_4 = ""
    # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        audio_4 = "MND/MND4.m4a"
    elif data.language_used == "Hokkien":
        audio_4 = "HOK/HOK4.m4a"
    else:
        audio_4 = "CEB/CEB4.m4a"

    if request.method == 'POST':
        if form.is_valid():
            data.idnumber = request.POST.get('idnumber')
            data.save()
            return HttpResponseRedirect('../page5')
           
    context = {
        'form': form,
        'audio_4': audio_4 
    }
    return render(request, 'main/page4.html', context)

def page5(request):
    data = Participant.objects.latest('id')
    form = AgeForm(request.POST)
    audio_4 = ""
    # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        audio_5 = "MND/MND5.m4a"
    elif data.language_used == "Hokkien":
        audio_5 = "HOK/HOK5.m4a"
    else:
        audio_5 = "CEB/CEB5.m4a"

    if request.method == 'POST':
        if form.is_valid():
            data.age = request.POST.get('age')
            data.save()
            return HttpResponseRedirect('../page6')
           
    context = {
        'form': form,
        'audio_5': audio_5 
    }
    return render(request, 'main/page5.html', context)

def page6(request):
    data = Participant.objects.latest('id')
    form = GenderForm(request.POST)
    audio_6 = ""
    # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        audio_5 = "MND/MND5.m4a"
    elif data.language_used == "Hokkien":
        audio_5 = "HOK/HOK5.m4a"
    else:
        audio_5 = "CEB/CEB5.m4a"


    if request.method == 'POST':
        if form.is_valid():
            data.gender = request.POST.get('gender')
            data.save()
            return HttpResponseRedirect('../page7')
           
    context = {
        'form': form,
        'audio_6': audio_6 
    }
    return render(request, 'main/page6.html', context)

def page7(request):
    data = Participant.objects.latest('id')
    form = CollegeForm(request.POST)
    
    audio_7 = ""
    # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        audio_7 = "MND/MND7.m4a"
    elif data.language_used == "Hokkien":
        audio_7 = "HOK/HOK7.m4a"
    else:
        audio_7 = "CEB/CEB7.m4a"

    if request.method == 'POST':
        if form.is_valid():
            data.college = request.POST.get('college')
            data.save()
            return HttpResponseRedirect('../page8')
           
    context = {
        'form': form,
        'audio_7': audio_7 
    }
    return render(request, 'main/page7.html', context)

def page8(request):
    data = Participant.objects.latest('id')
    form = EmailForm(request.POST)
    
    audio_8 = ""
    # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        audio_8 = "MND/MND8.m4a"
    elif data.language_used == "Hokkien":
        audio_8 = "HOK/HOK8.m4a"
    else:
        audio_8 = "CEB/CEB8.m4a"

    if request.method == 'POST':
        if form.is_valid():
            data.email = request.POST.get('email')
            data.save()
            return HttpResponseRedirect('../page9')
           
    context = {
        'form': form,
        'audio_8': audio_8 
    }
    return render(request, 'main/page8.html', context)

def page9(request):
    data = Participant.objects.latest('id')
    form = MobileForm(request.POST)
    audio_9 = ""
    # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        audio_9 = "MND/MND9.m4a"
    elif data.language_used == "Hokkien":
        audio_9 = "HOK/HOK9.m4a"
    else:
        audio_9 = "CEB/CEB9.m4a"

    if request.method == 'POST':
        if form.is_valid():
            data.mobile = request.POST.get('mobile')
            data.save()
            return HttpResponseRedirect('../page10')
           
    context = {
        'form': form,
        'audio_9': audio_9
    }
    return render(request, 'main/page9.html', context)

def page10(request):
    data = Participant.objects.latest('id')
    audio_10_1 = ""
    audio_10_2 = ""
    audio_10_3 = ""
    audio_10_4 = ""
    audio_10_5 = ""
    audio_10_6 = ""
    audio_10_7 = ""
    audio_10_8 = ""
    # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        audio_10_1 = "MND/MND10.1.m4a"
        audio_10_2 = "MND/MND10.2.m4a"
        audio_10_3 = "MND/MND10.3.m4a"
        audio_10_4 = "MND/MND10.4.m4a"
        audio_10_5 = "MND/MND10.5.m4a"
        audio_10_6 = "MND/MND10.6.m4a"
        audio_10_7 = "MND/MND10.7.m4a"
        audio_10_8 = "MND/MND10.8.m4a"
        audio_10_9 = "MND/MND10.9.m4a"
    elif data.language_used == "Hokkien":
        audio_10_1 = "HOK/HOK10.1.m4a"
        audio_10_2 = "HOK/HOK10.2.m4a"
        audio_10_3 = "HOK/HOK10.3.m4a"
        audio_10_4 = "HOK/HOK10.4.m4a"
        audio_10_5 = "HOK/HOK10.5.m4a"
        audio_10_6 = "HOK/HOK10.6.m4a"
        audio_10_7 = "HOK/HOK10.7.m4a"
        audio_10_8 = "HOK/HOK10.8.m4a"
        audio_10_9 = "HOK/HOK10.9.m4a"
    else:
        audio_10_1 = "CEB/CEB10.1.m4a"
        audio_10_2 = "CEB/CEB10.2.m4a"
        audio_10_3 = "CEB/CEB10.3.m4a"
        audio_10_4 = "CEB/CEB10.4.m4a"
        audio_10_5 = "CEB/CEB10.5.m4a"
        audio_10_6 = "CEB/CEB10.6.m4a"
        audio_10_7 = "CEB/CEB10.7.m4a"
        audio_10_8 = "CEB/CEB10.8.m4a"
        audio_10_9 = "CEB/CEB10.9.m4a"
    
    context = {
        'audio_10_1': audio_10_1,
        'audio_10_2': audio_10_2,
        'audio_10_3': audio_10_3,
        'audio_10_4': audio_10_4,
        'audio_10_5': audio_10_5,
        'audio_10_6': audio_10_6,
        'audio_10_7': audio_10_7,
        'audio_10_8': audio_10_8,
        'audio_10_9': audio_10_9,
    }
    return render(request, 'main/page10.html', context)

def withdraw(request):
    data = Participant.objects.latest('id')
    data.withdraw_invest = "WITHDRAW"
    audio_10_9 = ""
    #TODO
    #payout 

     # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        audio_10_9 = "MND/MND10.9.m4a"
    elif data.language_used == "Hokkien":
        audio_10_9 = "HOK/HOK10.9.m4a"
    else:
        audio_10_9 = "CEB/CEB10.9.m4a"

    context = {
        'audio_10_9': audio_10_9,
    }
    data.save()
    return render(request, 'main/page13.html', context)

def invest(request):
    data = Participant.objects.latest('id')
    form = InvestAmountForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data.withdraw_invest = "INVEST"
            data.A_amount = request.POST.get('A_amount')
            data.B_amount = request.POST.get('B_amount')
            data.save()
            return HttpResponseRedirect('../page11')
           
    context = {
        'form': form,
    }
    return render(request, 'main/invest_amount.html', context)

def page11(request):
    data = Participant.objects.latest('id')
    if request.method == 'POST':
        data.A_gain_loss = request.POST.get('a_input')
        data.B_gain_loss = request.POST.get('b_input')
        data.save()
        return HttpResponseRedirect('../page12')
    return render(request, 'main/page11.html')

#TODO
#PAGE11 RESULT OF TABLE
def tableresult(request, id):
	data = Participant.objects.latest('id')
	context = {
		'data': data,
	}
	return render(request, 'main/page11.html', context)

def page12(request):
    data = Participant.objects.latest('id')
    if request.method == 'POST':
        return HttpResponseRedirect('../page13')
    context = {
        'data': data,
    }
    return render(request, 'main/page12.html', context)

def page13(request):
    data = Participant.objects.latest('id')
    closing_line = ""
    # if data.language_used == "English":
       
    # elif data.language_used == "Tagalog":
       
    # elif data.language_used == "Korean":
       
    # elif data.language_used == "Japanese":
       
    if data.language_used == "Mandarin":
        closing_line = "謝謝您參與研究!"
    elif data.language_used == "Hokkien":
        closing_line = "謝謝您參與研究!"
    else:
        closing_line = "Salamat sa pag apil sa amoang eksperimento!"

    context = {
        'data': data,
        'closing_line' : closing_line
    }
    return render(request, 'main/page13.html', context)

