from django.urls import path
from .views import home, nosotros

urlpatterns = [
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
]
