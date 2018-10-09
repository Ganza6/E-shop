from django.shortcuts import render
from products.models import *
def main(request):
    products_images = ProductImage.objects.filter(is_active=True,is_main = True)
    # products_images_cups = products_images.filter()
    # products_images_teapots = products_images.filter()
    return render(request, 'main\main.html',locals())
