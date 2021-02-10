from django.contrib import admin

# Register your models here.
from django.contrib import admin
from questions.models import Question, QuestionOptions

admin.site.register(Question)
admin.site.register(QuestionOptions)