# -*- coding: utf-8 -*-
from django import forms
from .models import *


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = [""]


class LoginForm(forms.Form):
    email = forms.CharField(label=u'Логин/Email',
                            required=True)
    password = forms.CharField(widget=forms.PasswordInput,
                               label=u'Пароль',
                               required=True)
    keep_logged = forms.BooleanField(required=False,
                                     label=u'Запомнить',
                                     initial=True)
    # captcha = CaptchaField(label=u'', )

    # layout = Layout(Row('email', 'password'),
    #                'captcha',
    #                'keep_logged')

    def do_authenticate(self, request):

        from django.contrib.auth import login, authenticate

        user = authenticate(username=request.POST['email'].lower(),
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            if not 'keep_logged' in request.POST:
                keep = True
            else:
                keep = self.cleaned_data['keep_logged']
            if keep:
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            return 0
        else:
            self.add_error(field='email',
                           error=u'')
            self.add_error(field='password',
                           error=u'Неверное имя пользователя или пароль')
            return 1


# Форма обратной СВЯЗИ


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)



