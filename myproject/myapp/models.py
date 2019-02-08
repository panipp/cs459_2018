from django.db import models
# Create your models here.
CATEGORY_CHOICES= (
('M', 'Meat'),
('V','Vegetable')
)

class Product(models.Model):
    name = models.CharField ( max_length = 20 )
    price = models.DecimalField ( max_digits = 5, decimal_places = 2 )
    category = models.CharField( max_length = 10, choices = CATEGORY_CHOICES, default = 'M' )
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
