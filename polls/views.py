# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import Choice, Question, Article
from django.utils import timezone
from .forms import SubscriberForm, LoginForm, ContactForm
from products.models import ProductImage
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


class IndexView(generic.ListView):
    name = "Qwerty"
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def form(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'polls/form.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'polls/../templates/library/home.html', locals())


def index1(request):
    return HttpResponse("Salam VOVAN")


def logon(request):
    d = {}

    if request.user.is_authenticated():
        return redirect('/polls/')

    else:
        if request.method == 'GET':
            d['login_form'] = LoginForm()
        else:
            login_form = LoginForm(request.POST)
            d['login_form'] = login_form
            if login_form.is_valid():
                if login_form.do_authenticate(request) == 0:
                    return redirect('/cabinet/')
            if 'captcha' in login_form.errors:
                login_form.add_error(field='',
                                     error=u'Неверно заполнено проверочное поле')

        return render(request, 'login.html', d)


# Форма обратной СВЯЗИ


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['udastan@mail.ru']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, 'email: ' + sender + ' message text: ' + message, 'dastan@onedrop.kz', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'thanks.html')
    else:
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу
    return render(request, 'contact.html', {'form': form})


# Start DJANGO BOOK models!!!
# Start DJANGO BOOK models!!!
# Start DJANGO BOOK models!!!


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'polls/year_archive.html', context)


def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year)
    b_list = a_list.objects.filter(pub_date__month=month)
    context = {'year': year, 'month': month, 'article_list': b_list}
    return render(request, 'polls/month_archive.html', context)
