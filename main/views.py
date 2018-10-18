from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, inlineformset_factory
from django.db.models import aggregates
from django.contrib import messages
import random
from decimal import Decimal

from main.models import Participant
from main.forms import TermsForm, LanguageForm, NameForm, AgeForm, GenderForm, CollegeForm
from main.forms import InvestAmountForm, OutcomeForm

from .models import Participant, Tally
# Create your views here.

def participants(request):
    data = Participant.objects.all().order_by('-id') 
        
    context = {
       'title': "Participants",
       'data':data,
    }
    return render(request, 'main/participants.html', context)

def index(request):
    participants = Participant.objects.all().count()
    ss = Participant.objects.filter(quadrant="SS")
    ww = Participant.objects.filter(quadrant="WW")
    sw = Participant.objects.filter(quadrant="SW")
    ws = Participant.objects.filter(quadrant="WS")

    ss_count = ss.count()
    ww_count = ww.count()
    sw_count = sw.count()
    ws_count = ws.count()

    ss_1=0
    ss_2=0
    for data in ss:
        if(data.treatment==1):
            ss_1=ss_1+1
        else:
            ss_2=ss_2+1

    ww_1=0
    ww_2=0
    for data in ww:
        if(data.treatment==1):
            ww_1=ww_1+1
        else:
            ww_2=ww_2+1

    sw_1=0
    sw_2=0
    for data in sw:
        if(data.treatment==1):
            sw_1=sw_1+1
        else:
            sw_2=sw_2+1
           
    ws_1=0
    ws_2=0
    for data in ws:
        if(data.treatment==1):
            ws_1=ws_1+1
        else:
            ws_2=ws_2+1

    if request.method == 'POST':
        messages.success(request, 'Data has been Saved!')
        Tally.objects.create(Participants= participants, SS=ss_count,WW=ww_count,SW=sw_count,WS=ws_count,
        SS1=ss_1,SS2=ss_2,WW1=ww_1,WW2=ww_2, SW1=sw_1,SW2=sw_2,WS1=ws_1,WS2=ws_2)
        return HttpResponseRedirect('../index')

    context = {
        'title': "Tally",
        'ss_count': ss_count,
        'ww_count': ww_count,
        'sw_count': sw_count,
        'ws_count': ws_count,
        'ss_1': ss_1,
        'ss_2': ss_2,
        'ww_1': ww_1,
        'ww_2': ww_2,
        'sw_1': sw_1,
        'sw_2': sw_2,
        'ws_1': ws_1,
        'ws_2': ws_2,
        'participants':participants,
    }
    return render(request, 'main/index.html', context)

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
            #treatment data
            if data.language_used == data.first_language:
                data.treatment = 1
            else:
                data.treatment = 2

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
    form = NameForm(request.POST or None)
    audio_3 = ""
    if data.language_used == "English":
        audio_3 = "ENG/ENG3.mp3"
    elif data.language_used == "Tagalog":
        audio_3 = "TAG/TAG3.mp3"
    elif data.language_used == "Korean":
        audio_3 = "KOR/KOR3.mp3"
    elif data.language_used == "Japanese":
        audio_3 = "JAP/JAP3.mp3"
    elif data.language_used == "Mandarin":
        audio_3 = "MND/MND3.mp3"
    elif data.language_used == "Hokkien":
        audio_3 = "HOK/HOK3.mp3"
    else:
        audio_3 = "CEB/CEB3.mp3"

    if request.method == 'POST':
        if form.is_valid():
            print("vaid")
            data.name = request.POST.get('name')
            data.save()
            return HttpResponseRedirect('../page4')
        else:
            print("not valid")
    context = {
        'form': form,
        'audio_3': audio_3 
    }
    return render(request, 'main/page3.html', context)


# def page4(request):
#     data = Participant.objects.latest('id')
#     form = IDForm(request.POST)

#     audio_4 = ""
#     if data.language_used == "English":
#         audio_4 = "ENG/ENG4.mp3"
#     elif data.language_used == "Tagalog":
#         audio_4 = "TAG/TAG4.mp3"
#     elif data.language_used == "Korean":
#         audio_4 = "KOR/KOR4.mp3"
#     elif data.language_used == "Japanese":
#         audio_4 = "JAP/JAP4.mp3"
#     elif data.language_used == "Mandarin":
#         audio_4 = "MND/MND4.mp3"
#     elif data.language_used == "Hokkien":
#         audio_4 = "HOK/HOK4.mp3"
#     else:
#         audio_4 = "CEB/CEB4.mp3"

#     if request.method == 'POST':
#         if form.is_valid():
#             data.idnumber = request.POST.get('idnumber')
#             data.save()
#             return HttpResponseRedirect('../page5')
           
#     context = {
#         'form': form,
#         'audio_4': audio_4 
#     }
#     return render(request, 'main/page4.html', context)

def page5(request):
    data = Participant.objects.latest('id')
    form = AgeForm(request.POST)
    audio_5 = ""
    if data.language_used == "English":
        audio_5 = "ENG/ENG5.mp3"
    elif data.language_used == "Tagalog":
        audio_5 = "TAG/TAG5.mp3"
    elif data.language_used == "Korean":
        audio_5 = "KOR/KOR5.mp3"
    elif data.language_used == "Japanese":
        audio_5 = "JAP/JAP5.mp3"
    elif data.language_used == "Mandarin":
        audio_5 = "MND/MND5.mp3"
    elif data.language_used == "Hokkien":
        audio_5 = "HOK/HOK5.mp3"
    else:
        audio_5 = "CEB/CEB5.mp3"

    if request.method == 'POST':
        if form.is_valid():
            data.age = request.POST.get('age')
            data.save()
            return HttpResponseRedirect('../page5')
           
    context = {
        'form': form,
        'audio_5': audio_5 
    }
    return render(request, 'main/page5.html', context)

def page6(request):
    data = Participant.objects.latest('id')
    form = GenderForm(request.POST)
    audio_6 = ""
    if data.language_used == "English":
        audio_6 = "ENG/ENG6.mp3"
    elif data.language_used == "Tagalog":
        audio_6 = "TAG/TAG6.mp3"
    elif data.language_used == "Korean":
        audio_6 = "KOR/KOR6.mp3"
    elif data.language_used == "Japanese":
        audio_6 = "JAP/JAP6.mp3"
    elif data.language_used == "Mandarin":
        audio_6 = "MND/MND6.mp3"
    elif data.language_used == "Hokkien":
        audio_6 = "HOK/HOK6.mp3"
    else:
        audio_6 = "CEB/CEB6.mp3"


    if request.method == 'POST':
        if form.is_valid():
            data.gender = request.POST.get('gender')
            data.save()
            return HttpResponseRedirect('../page6')
           
    context = {
        'form': form,
        'audio_6': audio_6 
    }
    return render(request, 'main/page6.html', context)

def page7(request):
    data = Participant.objects.latest('id')
    form = CollegeForm(request.POST)
    audio_7 = ""
    if data.language_used == "English":
        audio_7 = "ENG/ENG7.mp3"
    elif data.language_used == "Tagalog":
        audio_7 = "TAG/TAG7.mp3"
    elif data.language_used == "Korean":
        audio_7 = "KOR/KOR7.mp3"
    elif data.language_used == "Japanese":
        audio_7 = "JAP/JAP7.mp3"
    elif data.language_used == "Mandarin":
        audio_7 = "MND/MND7.mp3"
    elif data.language_used == "Hokkien":
        audio_7 = "HOK/HOK7.mp3"
    else:
        audio_7 = "CEB/CEB7.mp3"

    if request.method == 'POST':
        if form.is_valid():
            data.college = request.POST.get('college')
            data.save()
            return HttpResponseRedirect('../page7')
           
    context = {
        'form': form,
        'audio_7': audio_7 
    }
    return render(request, 'main/page7.html', context)

# def page8(request):
#     data = Participant.objects.latest('id')
#     form = EmailForm(request.POST)
#     audio_8 = ""
#     if data.language_used == "English":
#         audio_8 = "ENG/ENG8.mp3"
#     elif data.language_used == "Tagalog":
#         audio_8 = "TAG/TAG8.mp3"
#     elif data.language_used == "Korean":
#         audio_8 = "KOR/KOR8.mp3"
#     elif data.language_used == "Japanese":
#         audio_8 = "JAP/JAP8.mp3"
#     elif data.language_used == "Mandarin":
#         audio_8 = "MND/MND8.mp3"
#     elif data.language_used == "Hokkien":
#         audio_8 = "HOK/HOK8.mp3"
#     else:
#         audio_8 = "CEB/CEB8.mp3"

#     if request.method == 'POST':
#         if form.is_valid():
#             data.email = request.POST.get('email')
#             data.save()
#             return HttpResponseRedirect('../page9')
           
#     context = {
#         'form': form,
#         'audio_8': audio_8 
#     }
#     return render(request, 'main/page8.html', context)

# def page9(request):
#     data = Participant.objects.latest('id')
#     form = MobileForm(request.POST)
#     audio_9 = ""
#     if data.language_used == "English":
#         audio_9 = "ENG/ENG9.mp3"
#     elif data.language_used == "Tagalog":
#         audio_9 = "TAG/TAG9.mp3"
#     elif data.language_used == "Korean":
#         audio_9 = "KOR/KOR9.mp3"
#     elif data.language_used == "Japanese":
#         audio_9 = "JAP/JAP9.mp3"
#     elif data.language_used == "Mandarin":
#         audio_9 = "MND/MND9.mp3"
#     elif data.language_used == "Hokkien":
#         audio_9 = "HOK/HOK9.mp3"
#     else:
#         audio_9 = "CEB/CEB9.mp3"


#     if request.method == 'POST':
#         if form.is_valid():
#             data.mobile = request.POST.get('mobile')
#             data.save()
#             return HttpResponseRedirect('../page10')
           
#     context = {
#         'form': form,
#         'audio_9': audio_9
#     }
#     return render(request, 'main/page9.html', context)

def page10(request):
    data = Participant.objects.latest('id')
    audio_10_1 = ""
    if data.language_used == "English":
        audio_10_1 = "ENG/ENG10.1-10.6.mp3"
    elif data.language_used == "Tagalog":
        audio_10_1 = "TAG/TAG10.1-10.6.mp3"
    elif data.language_used == "Korean":
        audio_10_1 = "KOR/KOR10.1-10.6.mp3"
    elif data.language_used == "Japanese":
        audio_10_1 = "JAP/JAP10.1-10.6.mp3"
    elif data.language_used == "Mandarin":
        audio_10_1 = "MND/MND10.1-1.06.mp3"
    elif data.language_used == "Hokkien":
        audio_10_1 = "HOK/HOK10.1-10.6.mp3"
    else:
        audio_10_1 = "CEB/CEB10.1-10.6.mp3"
       
    context = {
        'audio_10_1': audio_10_1,
    }
    return render(request, 'main/page10.html', context)

def withdraw(request):
    data = Participant.objects.latest('id')
    data.withdraw_invest = 1
    data.save()
    return HttpResponseRedirect('../page10')

def invest(request):
    data = Participant.objects.latest('id')
    data.withdraw_invest = 2
    form = InvestAmountForm(request.POST)
    audio_10_2 = ""

    if data.language_used == "English":
        audio_10_2 = "ENG/ENG10.7-10.11.mp3"
    elif data.language_used == "Tagalog":
        audio_10_2 = "TAG/TAG10.7-10.10.mp3"
    elif data.language_used == "Korean":
        audio_10_2 = "KOR/KOR10.7-10.10.mp3"
    elif data.language_used == "Japanese":
        audio_10_2 = "JAP/JAP10.7-10.10.mp3"
    elif data.language_used == "Mandarin":
        audio_10_2 = "MND/MND10.7-10.10.mp3"
    elif data.language_used == "Hokkien":
        audio_10_2 = "HOK/HOK10.7-10.10.mp3"
    else:
        audio_10_2 = "CEB/CEB10.7-10.10.mp3"

    if request.method == 'POST':
        if form.is_valid():
            data.withdraw_invest = 2
            data.A_generated_percent = request.POST.get('percent_A')
            data.B_generated_percent = request.POST.get('percent_B')
            data.A_amount =  request.POST.get('A_amount')
            data.B_amount =  request.POST.get('B_amount')
            data.save()
            return HttpResponseRedirect('../table-data')

    context = {
        'form': form,
        'audio_10_2': audio_10_2,
    }
    return render(request, 'main/invest_amount.html', context)

def page11(request):
    data = Participant.objects.latest('id')
    form = OutcomeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            a_output = request.POST.get('A_gain_loss')
            b_output = request.POST.get('B_gain_loss')

            data.A_gain_loss = Decimal(a_output)
            data.B_gain_loss = Decimal(b_output)
            data.save()
            return HttpResponseRedirect('../page9')
        
    context = {
		'data': data,
        'form': form,
	}
    return render(request, 'main/page11.html', context)


def table_data(request):
    data = Participant.objects.latest('id')
    # TABLE OUTPUT LOWEST POSSIBLE
    lgla = data.A_amount * Decimal(-49.90/100)
    lglb = data.B_amount * Decimal(-7.00/100)
    lgla_output = round(lgla,2)
    lglb_output = round(lglb,2)
    lgl_total = lgla_output + lglb_output
    lgla_total = data.A_amount + lgla_output
    lglb_total = data.B_amount + lglb_output
    lgl_end_total = lgla_total + lglb_total 

    #TABLE OUTPUT HIGHEST POSSIBLE
    hgla = data.A_amount * Decimal(96.90/100)
    hglb = data.B_amount * Decimal(13/100)
    hgla_output = round(hgla,2)
    hglb_output = round(hglb,2)
    hgl_total = hgla_output + hglb_output
    hgla_total = data.A_amount + hgla_output
    hglb_total = data.B_amount + hglb_output
    hgl_end_total = hgla_total + hglb_total 

    #OUTCOME
    percent_a = random.uniform(-49.90, 96.90)
    percent_b = random.uniform(-7.00, 13)
    percent_a_output = round(percent_a,2)
    percent_b_output = round(percent_b,2)
    aa_output = data.A_amount * Decimal(percent_a_output/100)
    bb_output = data.B_amount * Decimal(percent_b_output/100)
    a_output = round(aa_output,2)
    b_output = round(bb_output,2)
    
    context = {
        'data': data,
        'lgla_output':lgla_output,
        'lglb_output':lglb_output,
        'lgl_total':lgl_total,
        'lgla_total':lgla_total,
        'lglb_total':lglb_total,
        'lgl_end_total':lgl_end_total,
        'hgla_output':hgla_output,
        'hglb_output':hglb_output,
        'hgl_total':hgl_total,
        'hgla_total':hgla_total,
        'hglb_total':hglb_total,
        'hgl_end_total':hgl_end_total,
    }
    return render(request, 'main/table_data.html', context)

def page12(request):
    data = Participant.objects.latest('id')
    if request.method == 'POST':
        return HttpResponseRedirect('../page10')
    context = {
        'data': data,
    }
    return render(request, 'main/page12.html', context)

def page13(request):
    data = Participant.objects.latest('id')
    closing_line = ""
    if data.language_used == "English":
        closing_line = "Thank you for participating in our experiment!"
    elif data.language_used == "Tagalog":
        closing_line = "Salamat sa paglahok sa aming eksperimento!"
    elif data.language_used == "Korean":
        closing_line = "설문조사에 참여해주셔서 감사합니다!"
    elif data.language_used == "Japanese":
        closing_line = "参加していただきありがとうございます!"
    elif data.language_used == "Mandarin":
        closing_line = "謝謝您參與研究!"
    elif data.language_used == "Hokkien":
        closing_line = "謝謝您參與研究!"
    else:
        closing_line = "Salamat sa pag apil sa amoang eksperimento!"

    print(data.language_used)

    context = {
        'data': data,
        'closing_line' : closing_line
    }
    return render(request, 'main/page13.html', context)

