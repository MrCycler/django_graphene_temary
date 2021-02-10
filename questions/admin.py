from django.contrib import admin

# Register your models here.
from django.contrib import admin
from questions.models import Question, QuestionOption

admin.site.register(Question)
admin.site.register(QuestionOption)