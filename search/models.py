from django.db import models

# Create your models here.
class Products(models.Model):
    
	INSTOCK_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
	
	title = models.CharField(max_length=100)
	brand = models.IntegerField()
	store = models.IntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	in_stock = models.BooleanField(choices=INSTOCK_CHOICES, default=False)
	