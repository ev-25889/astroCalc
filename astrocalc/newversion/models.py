from django.db import models

class Data(models.Model):
    # id = models.CharField('Key', max_length=50, primary_key=True)
    name = models.CharField('Name', max_length=100)
    birthday = models.DateField('Birthday')
    city = models.CharField('City', max_length=200)
    street = models.CharField('Street', max_length=200)
    house = models.CharField('House', max_length=50)
    date_create = models.DateField('date_create', auto_now_add=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Данные'
        verbose_name_plural = 'Данные'
