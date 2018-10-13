from django.urls import path
from . import views
urlpatterns = [
        path('',views.product),
        path('<int:product_id>', views.product),
 ]




