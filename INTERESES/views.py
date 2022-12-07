from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import *


# Create your views here.

def index(request):
    return render(request, 'INTERESES/index.html')


def test(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
    except(KeyError, Test.DoesNotExist):
        return HttpResponse("none")
    else:
        questions = test.question_set.all()
        context = {
            'test': test,
            'questions': questions,
        }
        return render(request, 'INTERESES/test.html', context)


def save(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
        questions = test.question_set.all()
        values = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }
        for i in range(1, questions.count() + 1):
            attr = request.POST['question[' + str(i) + ']']
            values[int(attr)] += 1
        t = dict()
        for key, value in values.items():
            per = Percentage.objects.get(attribute__exact=key, sum__exact=value)
            t[key] = per
    except(KeyError, Test.DoesNotExist):
        return HttpResponse("none")
    else:
        answer = Answer(
            user=User.objects.get(pk=1),
            test=test,
        )
        answer.save()
        answer.attributes.add(*list(t.values()))
        return HttpResponseRedirect(reverse('INTERESES:certificate', args=(answer.id,)))


"""
def save(request, test_id):
    try:
        test = Test.objects.get(pk=test_id)
        questions = test.question_set.all()
    except(KeyError, Test.DoesNotExist):
        return HttpResponse("none")
    else:
        values = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }
        for i in range(1, questions.count() + 1):
            attr = request.POST['question[' + str(i) + ']']
            values[int(attr)] += 1
        t = dict()
        for key, value in values.items():
            per = Percentage.objects.get(attribute__exact=key, sum__exact=value)
            t[key] = per.percentage
        id_max = max(t, key=t.get)
        id_min = min(t, key=t.get)
        max_attr = Attribute.objects.get(id__exact=id_max).attribute
        min_attr = Attribute.objects.get(id__exact=id_min).attribute

        return HttpResponse("<br> %s <br> max is: %s <br> min is: %s" % (t, max_attr, min_attr))
"""


def certificate(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    attributes = answer.attributes.all().order_by('-percentage')
    max_attr = attributes[0]
    max_variant = max_attr.attribute.attributes.get(variant="Alto")
    min_attr = attributes[4]
    min_variant = min_attr.attribute.attributes.get(variant="Bajo")
    context = {
        'answer': answer,
        'attributes': attributes,
        'max_attr': attributes[0],
        'max_variant': max_variant,
        'min_attr': min_attr,
        'min_variant': min_variant,
        'variants': [max_variant, min_variant]
    }
    return render(request, 'INTERESES/certificate.html', context=context)
