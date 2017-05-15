# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone


class EducationalMaterials(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None,
                            verbose_name='Название учебного материяла')
    author = models.ForeignKey('Author', verbose_name='Автор(ы)')
    date_of_writing = models.DateField(verbose_name='Дата создание учебного материяла',
                                       auto_now=False, auto_now_add=False)
    type_of_material = models.ForeignKey('TypeOfMaterial', verbose_name='Вид учебного материяла')
    theme_of = models.ForeignKey('ThemeOf', verbose_name='Направление учебного материяла')
    short_description = models.TextField(blank=True, null=True, default=None, verbose_name='Краткое описание')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Полное описание')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    book = models.FileField(verbose_name='Книга', upload_to='books/')

    def __unicode__(self):
        return "%s, %s" % (self.name, self.author)

    class Meta:
        verbose_name = 'Учебный материал'
        verbose_name_plural = 'Учебные материалы'


class TypeOfMaterial(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип учебника'
        verbose_name_plural = 'Типы учебников'


class ThemeOf(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Тематика учебного материала'
        verbose_name_plural = 'Тематики учебных материалов'


class Author(models.Model):
    full_name = models.CharField(max_length=32, blank=True, null=True, default=None)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class MaterialImage(models.Model):
    product = models.ForeignKey(EducationalMaterials, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='material_image/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Обложка'
        verbose_name_plural = 'Обложки'