from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.EdgarModel)
class EdgarAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


@admin.register(models.FeedbackModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']