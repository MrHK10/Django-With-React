from django.contrib import admin

# Register your models here.
# questionnaire/admin.py

from django.contrib import admin
from .models import Language, Question, Answer

admin.site.register(Language)
admin.site.register(Question)
admin.site.register(Answer)
