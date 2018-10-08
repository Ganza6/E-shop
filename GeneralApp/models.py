from django.db import models

class Person(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Note = models.CharField(max_length=255,blank=True)
    Time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return self.Name
