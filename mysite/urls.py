from django.urls import path

from .views import home,AutoTheftStolen,CasesPropertyStolen,TotalKidnapp,TotalMurder,TotalRape,TotalCluster

urlpatterns = [
    path('',home, name='home'),
    path('auto-theft/',AutoTheftStolen, name='auto-theft'),
    path('property-stolen/',CasesPropertyStolen, name='property-stolen'),
    path('total-kidnapp/',TotalKidnapp, name='total-kidnapp'),
    path('total-murder/',TotalMurder, name='total-murder'),
    path('total-rape/',TotalRape, name='total-rape'),
    path('total-cluster/',TotalCluster, name='total-cluster'),
]