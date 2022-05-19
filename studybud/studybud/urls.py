from django.contrib import admin
from django.urls import path
from django.https import HttpResponse


def home(request):
    return HttpResponse('HOME PAGE')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
