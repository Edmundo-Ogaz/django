from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import *

# Create your views here.

def index(request):
    return render(request, 'DISC/index.html')


def test(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
    except(KeyError, Test.DoesNotExist):
        return HttpResponse("none")
    else:
        cards = test.card_set.all()
        context = {
            'test': test,
            'cards': cards,
        }
        return render(request, 'DISC/test.html', context)


def save(request, test_id):
    test = Test.objects.get(pk=test_id)
    # ANSWER
    card_count = test.card_set.count()
    mas = ""
    menos = ""
    values = {
        "D": 0,
        "I": 0,
        "E": 0,
        "C": 0
    }
    segment = [0, 0, 0, 0]
    scores = [
        [-29, -8, -4, -1, 1, 4, 8],
        [-29, -8, -4, -2, 1, 3, 6],
        [-29, -11, -7, -4, 1, 2, 7],
        [-29, -6, -3, -1, 2, 4, 8]
    ]
    try:
        ##GET "SELECTED" ANSWER
        for i in range(card_count):
            name_mas = "mas[" + str(i) + "]"
            post_mas = request.POST[name_mas]
            mas += post_mas
            values[post_mas] += 1
            name_menos = "menos[" + str(i) + "]"
            post_menos = request.POST[name_menos]
            menos += post_menos
            values[post_menos] -= 1
        values_keys = list(values.keys())
        for i in range(4):
            for j in range(7):
                if values[values_keys[i]] > scores[i][j]:
                    segment[i] += 1
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return HttpResponse("asdkasdja")
    else:
        resp = ""
        db_segment_n = segment[0]*1000 + segment[1]*100 + segment[2]*10 + segment[3]
        db_segment = Segment.objects.get(pk=db_segment_n)
        answer = Answer(
            positive=mas,
            negative=menos,
            D=values["D"],
            I=values["I"],
            S=values["E"],
            C=values["C"],
            ans_date=timezone.now(),
            segment=db_segment,
            user=User.objects.get(pk=1),
            test=test,
        )
        answer.save()
        return HttpResponseRedirect(reverse('DISC:certificate', args=(answer.id,)))


def certificate(request, answer_id):
    try:
        answer = Answer.objects.get(pk=answer_id)
        profile = answer.segment.profile
    except(KeyError, Test.DoesNotExist):
        return HttpResponse("none")
    else:
        context = {
            "answer": answer,
            "profile": profile,
        }
        return render(request, 'DISC/certificate.html', context)
        return HttpResponse("%s" % "sws")
