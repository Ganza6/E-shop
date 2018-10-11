from django.urls import path
from . import views
urlpatterns = [
    # cо 2 джангой не работал - прокомментировать урлы не могу, но здорово давать имена урлам, чтоб можно было указывать
    # их в темплейтах не хардкодя
    path("", views.GeneralApp),
    path("succsess",views.succsess),
]




