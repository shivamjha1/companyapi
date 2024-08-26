from django.urls import path,include
from . import views
from rest_framework import routers

from .views import CompanyViewset,EmployeeViewset,PersonalViewset


router=routers.DefaultRouter()
router.register(r"company",CompanyViewset)
router.register(r"employee",EmployeeViewset)
router.register(r"personal_details",PersonalViewset)

urlpatterns = [
    path('home',views.index),
    path('',include(router.urls)),
]
