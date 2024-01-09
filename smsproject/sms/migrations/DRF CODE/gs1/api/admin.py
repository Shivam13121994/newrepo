from django.contrib import admin
from .models import Student  # first make model in models.py then import that Student model then register it

# Register your models here.
@admin.register(Student) 
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']  # for what you want to display
      
