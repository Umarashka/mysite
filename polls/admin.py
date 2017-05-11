from django.contrib import admin
from .models import *
import models


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')


class SubscriberAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name']
    search_fields = ['name', 'email']

    fields = ['email']

    class Meta:
        model = Subscriber


admin.site.register(Question, QuestionAdmin)
admin.site.register(Subscriber, SubscriberAdmin)

# Start DJANGO BOOK models!!!
# Start DJANGO BOOK models!!!
# Start DJANGO BOOK models!!!

admin.site.register(models.Article)
admin.site.register(models.Reporter)

