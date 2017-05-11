# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from products.models import Product


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # total price for all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


# Start DJANGO BOOK models!!!
# Start DJANGO BOOK models!!!
# Start DJANGO BOOK models!!!

# class Reporter(models.Model):
#     full_name = models.CharField(max_length=70)
#
#     def __str__(self):
#         return self.full_name
#
#
# class Article(models.Model):
#     pub_date = models.DateField()
#     headline = models.CharField(max_length=70)
#     content = models.TextField()
#     reporter = models.ForeignKey(Reporter)
#
#     def __str__(self):
#         return self.headline


# class Person(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     first_name = models.CharField("person's first name", max_length=30)
#     last_name = models.CharField(max_length=30)
#     # name = models.CharField(max_length=128)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
#     birth_day = models.DateField()
#
#     def baby_boomer_status(self):
#         "Returns the person’s baby-boomer status."
#         import datetime
#         if self.birth_date < datetime.date(1945, 8, 1):
#             return "Pre-boomer"
#         elif self.birth_date < datetime.date(1965, 1, 1):
#             return "Baby boomer"
#         else:
#             return "Post-boomer"
#
#     def _get_full_name(self):
#         "Returns the person’s full name."
#         return '%s %s' % (self.first_name, self.last_name)
#
#     full_name = property(_get_full_name)
#
#     def __str__(self):
#         return self.name


# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')
#
#     def __str__(self):
#         return self.name
#
#
# class Membership(models.Model):
#     person = models.ForeignKey(Person)
#     group = models.ForeignKey(Group)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)


# class Musician(models.Model):
#     firs_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)
#
#
# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()
#
#
# class Fruit(models.Model):
#     name = models.CharField(max_length=100, primary_key=True)


# class Manufacturer(models.Model):
#     # ...
#     pass
#
#
# class Car(models.Model):
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#     # ...


# class Topping(models.Model):
#     # ...
#     pass
#
#
# class Pizza(models.Model):
#     # ...
#     toppings = models.ManyToManyField(Topping)


# class Ox(models.Model):
#     horn_length = models.IntegerField()
#
#     class Meta:
#         ordering = ["horn_length"]
#         verbose_name_plural = "oxen"
#
#
# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     def save(self, *args, **kwargs):
#         if self.name == "Yoko Ono’s blog":
#             return  # Yoko shall never have her own blog!
#         else:
#             super(Blog, self).save(*args, **kwargs)  # Call the "real" save() method.
#
#
# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()
#
#     class Meta:
#         abstract = True
#
#
# class Student(CommonInfo):
#     home_group = models.CharField(max_length=5)


# class CommonUserInfo(models.Model):
#     # ...
#     class Meta:
#         abstract = True
#         ordering = ['name']
#
#
# class StudentInfo(CommonUserInfo):
#     # ...
#     class Meta(CommonUserInfo.Meta):
#         db_table = 'student_info'


# class Place(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=80)
#
#
# class Restaurant(Place):
#     service_hot_dogs = models.BooleanField(default=False)
#     service_pizza = models.BooleanField(default=False)
#
#
# class Supplier(Place):
#     customers = models.ManyToManyField(Place, related_name='provider')
#
#
# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#
#
# class MyUser(Person):
#     class Meta:
#         proxy = True

# End DJANGO BOOK models!!!


