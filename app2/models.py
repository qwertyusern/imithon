from django.db import models

from app1.models import Muallif


class Maqola(models.Model):
    sarlavha=models.CharField(max_length=125)
    sana=models.DateField(auto_now_add=True)
    mavzu=models.CharField(max_length=125)
    matn=models.TextField()
    muallif=models.ForeignKey(Muallif,on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha


