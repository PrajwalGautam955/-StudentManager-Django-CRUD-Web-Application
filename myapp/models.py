from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True , blank=True)
    roll = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return self.name
