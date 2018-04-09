from django.contrib import admin
from .models import News,NewsAdmin
from .models import Question,QuestionAdmin

# Register your models here.

admin.site.register(News,NewsAdmin)
admin.site.register(Question,QuestionAdmin)