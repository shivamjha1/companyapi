from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage),
    path("emp/<slug:slug>/",views.emp,name="slug"),
    path("apix",views.apiex),
]
