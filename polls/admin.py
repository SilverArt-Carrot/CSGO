from django.contrib import admin
from .models import Question, Choice


# Register your models here.
# admin.site.register(Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Time', {'fields': ['pub_date']}),
        ('Date Information', {'fields': ['question_text']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
