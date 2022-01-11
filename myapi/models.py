from django.db import models

class PK(models.Model):
    name = models.CharField('название комплектующих', max_length=200)
    image = models.TextField('URL изоображения', max_length=5000)
    price = models.CharField('Цена', max_length=200)
    description = models.TextField('Описание', max_length=5000)
    displei = models.CharField('Дисплей', max_length=200)
    processor = models.CharField('Процессор', max_length=200)
    operativka = models.CharField('Оперативка', max_length=200)
    nakopiteli = models.CharField('Накопитель', max_length=200)
    ves = models.CharField('Вес', max_length=200)
    def __str__(self):
        return self.name

class Purchase(models.Model):
    product = models.ForeignKey(PK, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

