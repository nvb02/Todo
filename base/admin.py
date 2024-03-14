from django.contrib import admin
from .models import Todo #calling model.py to get the todo table, '.' goes outside of this file to the folder area

# Register your models here.
admin.site.register(Todo) #Todo class is defined in admin panel, the data from the table can be seen, changed etc