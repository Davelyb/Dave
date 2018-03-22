from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'pub_date', ]
    # fields = ['pub_date', 'question_text',]
    fieldsets = [
        ('Title',           {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date', 'question_text']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
admin.site.register(Choice)
