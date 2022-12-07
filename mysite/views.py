from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta

# Create your views here.

from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.urls import reverse


def index(request):
    return HttpResponse("holahola")

