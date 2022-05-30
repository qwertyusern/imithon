
from django.contrib import admin
from django.urls import path, include

from app1.views import KirishView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', KirishView.as_view(), name="kirish"),
    path('user/', include("app1.urls")),
    path('maqola/', include("app2.urls")),
]
