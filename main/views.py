from django.shortcuts import render
from products.models import ProductImage


def main(request):
    products_images = ProductImage.objects.filter(is_available=True,is_main = True)
    products_images_cups = products_images.filter(product__type__id=2)
    products_images_teapots = products_images.filter(product__type__id=1)
    all_products = products_images.order_by('-product__price')
    bestsellers = give_bestsellers(all_products)
    return render(request, 'main/main.html',locals())


def give_bestsellers(all_products):#добавляем в "Хиты продаж" 4 самых дорогих товара из всех категорий, если категорий недостаточно
    types_number = set()#то расставляет все имеющиеся товары в шахматном порядке
    bestsellers = []
    for i in all_products:
        types_number.add(i.product.type)
    in_bestsellers = set()
    while len(bestsellers) < 4:
        in_bestsellers_type = set()
        for i in all_products:
            if i.product.type not in in_bestsellers_type and i not in in_bestsellers:
                bestsellers.append(i)
                in_bestsellers.add(i)
                in_bestsellers_type.add(i.product.type)
    return bestsellers
