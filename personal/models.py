from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=0, max_digits=5)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + '-' + str(self.id)


class Recycle(models.Model):
    Accessories='MA'
    Hard='HD'
    Mobile='MP'
    PC='PP'
    Others='O'
    choice_t = (
        (Accessories, 'Mobile Accessories'),
        (Hard, 'Hard Disk'),
        (Mobile, 'Mobile Phone'),
        (PC,'PC Parts'),
        (Others,'Others')
    )
    Type = models.CharField(max_length=20,choices=choice_t,default=Accessories)
    Image = models.FileField()
    Description = models.CharField(max_length=1000)
    Expected_price = models.DecimalField(decimal_places=0, max_digits=4)
    Name = models.CharField(max_length=250)
    Contact = models.DecimalField(decimal_places=0, max_digits=10)
    Address = models.CharField(max_length=1000)
    Gurugram='GG'
    Delhi='DL'
    Noida='N'
    Ghaziabad='GZB'
    choice_c = (
        (Gurugram, 'Gurugram'),
        (Delhi, 'Delhi'),
        (Noida, 'Noida'),
        (Ghaziabad,'Ghaziabad'),
    )
    City = models.CharField(max_length=20,choices=choice_c,default=Ghaziabad)



    def get_absolute_url(self):
        return reverse('detail_recycle', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name + '-' + str(self.id)








