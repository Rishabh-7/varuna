from django.db import models

# Create your models here.
class EmbData(models.Model):
    img = models.CharField(max_length=1400)
    email = models.EmailField(max_length=254)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lon = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return self.img