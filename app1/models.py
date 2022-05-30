from django.contrib.auth.models import User
from django.db import models

from app2.models import Maqola


class Muallif(models.Model):
    ism = models.CharField(max_length=45)
    yosh = models.SmallIntegerField()
    kasb = models.CharField(max_length=50)
    maqola = models.ForeignKey(Maqola, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.ism
