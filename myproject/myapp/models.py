from django.db import models
import qrcode
# Create your models here.
CATEGORY_CHOICES= (
('M', 'Meat'),
('V','Vegetable')
)

class Product(models.Model):
    name = models.CharField ( max_length = 20 )
    price = models.DecimalField ( max_digits = 5, decimal_places = 2 )
    category = models.CharField( max_length = 10, choices = CATEGORY_CHOICES, default = 'M' )

    def __str__(self):
        return self.name
    
    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        qr.add_data(self.name)
        qr.make(fit=True)
        img = qr.make_image()
        return img