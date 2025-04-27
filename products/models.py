from django.db import models

# Create your models here.
class Inverter(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    price=models.IntegerField()
    posted_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InverterFeature(models.Model):
    inverter = models.ForeignKey(Inverter, related_name='features', on_delete=models.CASCADE)
    feature = models.CharField(max_length=255)

    def __str__(self):
        return self.feature
