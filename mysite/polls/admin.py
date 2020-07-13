from django.contrib import admin
from .models import Question, Choice


class ChoiceAdmin(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceAdmin]
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date']})
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
