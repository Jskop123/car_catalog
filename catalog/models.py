from django.db import models
from django.utils.translation import gettext_lazy as _

class Index(models.Model):
    title = models.CharField(verbose_name=_('Tytuł'), max_length=100)
    description1 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")
    description2 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")
    description3 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")
    description4 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")
    description5 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")
    description6 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")
    description7 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")
    description8 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")
    description9 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")
    description10 = models.TextField(verbose_name=_('Opis'), blank=True, null=True, default="")

    def __str__(self):
        return self.title


class Car(models.Model):

    WITH_DRIVER = 'Z kierowcą'
    WITHOUT_DRIVER = 'Jeżdzący'
    CONSTANT = 'Stojący w miejscu'
    STATE_CHOICES = [
        (WITH_DRIVER, _('Jeżdzący')),
        (WITHOUT_DRIVER, _('Stojący')),
        (CONSTANT, _('Z kierowcą'))
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name=_('Nazwa'), max_length=50)
    description = models.CharField(verbose_name=_('Opis'), max_length=150)
    color = models.CharField(verbose_name=_('Kolor'), max_length=50, default='')
    rok = models.IntegerField(verbose_name=_('Rok'), default=0)
    stan = models.CharField(verbose_name=_('Stan'), max_length=30, choices=STATE_CHOICES, blank=True, null=True, default='Brak informacji')
    image1 = models.ImageField(blank=True, null=True, upload_to="images/")
    image2 = models.ImageField(blank=True, null=True, upload_to="images/", default='null')
    image3 = models.ImageField(blank=True, null=True, upload_to="images/", default='null')
    image4 = models.ImageField(blank=True, null=True, upload_to="images/", default='null')
    image5 = models.ImageField(blank=True, null=True, upload_to="images/", default='null')

    def __str__(self):
        return self.name


class Order(models.Model):

    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    ordered_cars = models.ManyToManyField("Car", through="OrderedCar")

    def __str__(self):
        return self.name

class OrderedCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
   

class Contact(models.Model):
    paragraph = models.CharField(max_length=200)
    adres = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


    

    
