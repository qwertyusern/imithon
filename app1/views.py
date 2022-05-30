from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.views import View


class KirishView(View):
    def get(self, request):
        return render(request, "kirish.html")
    def post(self, request):
        l = request.POST.get("l")
        p = request.POST.get("p")
        userlar = authenticate(request, username=l, password=p)
        if userlar is None:
            return redirect("login")
        login(request, userlar)
        return redirect("asosiy")
class LoginView(View):
    def get(self,request):
        return render(request,"login.html")
class LogoutView(View):
    def post(self,request):
        logout(request)
        redirect("kirish")
