from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()#unique=True для проверки уникальности вводимого mail
    note = models.CharField(max_length=255,blank=True)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Человек из формы обратной связи'
        verbose_name_plural = 'Люди из формы обратной связи'

    def __str__(self):
        return self.Name
