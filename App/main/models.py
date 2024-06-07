from django.db import models


class Car(models.Model):
    car_name = models.CharField('car_name', max_length=100)
    car_photo = models.ImageField('car_img', upload_to='uploads/')
    car_desc = models.TextField('car_description')
    car_price = models.IntegerField('car_price')


# Create your models here.
class Request(models.Model):
    user_name = models.CharField('user_name', max_length=100)
    user_phone_number = models.CharField('user_phone_number', max_length=100)
    user_car = models.ForeignKey(Car, on_delete=models.CASCADE)
