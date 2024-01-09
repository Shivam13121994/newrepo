from django.contrib import admin
# Register your models here.
from .models import SMSModel

# Register your models here.

@admin.register(SMSModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','Mobile_no']
