from django.urls import path
from . import views
urlpatterns = [
    path("", views.GeneralApp),
    path("succsess",views.succsess),
]




