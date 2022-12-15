from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime, timedelta

from .models import *

from django.utils import timezone
from django.urls import reverse

import logging

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.debug(__name__+' index')
    return render(request, 'IC/index.html')

def test(request, test_id):
    logger.debug(__name__+' test')
    test = Test.objects.get(pk=test_id)
    headers = Test.objects.get(pk=test_id).header_set.all()
    rows = Test.objects.get(pk=test_id).row_set.all()

    user = User.objects.get(pk=1)
    this_answer = Answer(answer="", score=0, correct=0, wrong=0, omitted=0,
                         ans_date=timezone.now(), test=test, user=user)
    this_answer.save()

    context = {
        'test': test,
        'headers': headers,
        'rows': rows,
        'answer': this_answer,
    }
    return render(request, 'IC/test.html', context)

def save(request, test_id):
    logger.debug(__name__+' save')
    test = Test.objects.get(pk=test_id)
    user = User.objects.get(pk=1)
    # ANSWER
    answer_id = request.POST['answer']
    flag = False
    try:
        ##GET "SELECTED" ANSWER
        this_answer = Answer.objects.get(pk=answer_id)
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return HttpResponse("asdkasdja")
    else:
        ##CHECK ANSWER
        if this_answer.user.id != user.id \
                or this_answer.ans_date.replace(tzinfo=None) > (datetime.now() + timedelta(minutes=8)) \
                or this_answer.state != "Iniciado":
            return HttpResponse("aslkdal123123123")
        else:
            binary_answer = "000000000000000000000000000000000000000000000000000000000000000000000000000"
            post = request.POST.getlist('check[]')

            for i in post:
                preb = binary_answer[:int(i)]
                postb = binary_answer[int(int(i) + 1):]
                binary_answer = preb + "1" + postb
            answer = binary_answer

            # SCORE
            guide = test.guide
            correct = 0
            not_selected = 0
            for i in range(len(guide)):
                if binary_answer[i] == guide[i]:
                    if binary_answer[i] == "1":
                        correct += 1
                    else:
                        not_selected += 1
            omitted = 19 - correct
            wrong = 56 - not_selected + omitted

            score = 0
            if wrong <= 1:
                score = 6
            elif 2 <= wrong <= 4:
                score = 5
            elif 5 <= wrong <= 7:
                score = 4
            elif 8 <= wrong <= 12:
                score = 3
            elif 13 <= wrong <= 17:
                score = 2
            else:
                score = 1

            this_answer.answer = answer
            this_answer.score = score
            this_answer.correct = correct
            this_answer.wrong = wrong
            this_answer.omitted = omitted
            this_answer.ans_date = timezone.now()
            this_answer.state = "Finalizado"
            # this_answer = Answer(answer=answer, score=score, correct=correct, wrong=wrong, omitted=omitted,
            #                     ans_date=timezone.now(), test=test, user=user)

            this_answer.save()

            return HttpResponseRedirect(reverse('IC:certificate', args=(this_answer.id,)))
            # return HttpResponse("%s." % this_answer.answer)

def tes(request):
    binary_answer = "000000000000000000000000000000000000000000000000000000000000000000000000000"
    binary_answer_t = "0000*0000*0000*0000*0000*0000*0000*0000*0000*0000*0000*0000*0000*0000*0000*"
    post = request.POST.getlist('check[]')
    asd = ""
    for i in post:
        preb = binary_answer[:int(i)]
        postb = binary_answer[int(int(i) + 1):]
        binary_answer = preb + "1" + postb
        asd += i
        asd += "<br>"
    return HttpResponse("%s" % binary_answer)


def certificate(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)

    score = answer.score
    if score == 1:
        level = "Nivel Bajo"
    elif score == 2:
        level = "Nivel Medio Bajo"
    elif score == 3:
        level = "Nivel Medio"
    elif score == 4:
        level = "Nivel Medio Alto"
    elif score == 5:
        level = "Nivel Alto"
    elif score == 6:
        level = "Nivel Muy Alto"

    context = {
        'score': score,
        'correct': answer.correct,
        'wrong': answer.wrong,
        'omitted': answer.omitted,
        'level': level,
        'date': answer.ans_date,
        'user': answer.user
    }
    return render(request, 'IC/certificate.html', context)

def list(request):
    logger.debug(__name__+' list')
    test = Test.objects.get(pk=1)

    context = {
        'test': test,
    }
    return render(request, 'IC/answer.html', context)
