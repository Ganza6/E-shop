from django.urls import path
from . import views


urlpatterns = [
    path("", views.general_app),
    path("success",views.success),
]




