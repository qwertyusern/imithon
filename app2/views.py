from django.shortcuts import render,redirect
from django.views import View

from app2.models import Maqola


class AsosiyView(View):
    def get(self,request):
        m=Maqola.objects.all()
        return render(request,"asosiy.html",{"maqola":m})

class MaqolaView(View):
    def get(self,request,pk):
        s=Maqola.objects.get(id=pk)
        return render(request,"maqola.html",{"sarlavha":s})


