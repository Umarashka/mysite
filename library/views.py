# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django import forms
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from . models import *


def library(request):
    materials_images = MaterialImage.objects.filter(is_active=True)
    return render(request, 'library/home.html', locals())

