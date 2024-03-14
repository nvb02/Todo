from django.db import models

# Create your models here.
class Todo(models.Model): # inheriting model class from django.db, table is formed in this class due to this class
    name = models.CharField(max_length=200) #charfield states that str data is stored in this object, max_length parameter exists in this class which needs to be fulfilled
    description = models.TextField() #textfield denotes huge length of texts
    status = models.CharField(max_length=200)
    