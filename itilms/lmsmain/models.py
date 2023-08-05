from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    photo_book=models.ImageField(upload_to='photos',null=True,blank=True)
    photo_author=models.ImageField(upload_to='photos',null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rent_price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rent_day=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rent_period=models.IntegerField(null=True,blank=True)
    active=models.BooleanField(default=True)
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rent', 'Rent'),
        ('sold', 'Sold'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title
    