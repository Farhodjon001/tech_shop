from django.db import models
from datetime import datetime

# Create your models here.

class PcModel(models.Model):
    model = models.CharField(max_length=200, default='')
    protcessor = models.CharField(max_length=50, default='')
    ram = models.IntegerField(default=0)
    ssd = models.IntegerField(default=0)
    hdd = models.IntegerField(default=0)

    objects=models.Manager

    def __str__(self):
        return self.model


class Payment(models.Model):
    pc_id=models.ForeignKey(PcModel,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    unit_price=models.IntegerField(default=0)
    date=models.DateTimeField(default=datetime.now)

    objects=models.Manager

