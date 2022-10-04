from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def index(request):
    activeIndex = '/'
    return render(request,
                  'shop/index.html',
                  {'activeIndex': activeIndex}
                  )

def product_list(request, category_slug=None):
    category = None
    activeShop = '/shop/'
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    contact_list = Product.objects.filter(available=True)
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        contact_list = contact_list.filter(category=category)
        paginator = Paginator(contact_list, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request,
                  'shop/shop.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'activeShop': activeShop,
                   'page_obj': page_obj,
                   'cart_product_form': cart_product_form}
                  )


# def product_detail(request, slug):
#     product = get_object_or_404(Product,
#                                 slug=slug,
#                                 available=True)
#     return render(request,
#                   'shop/shop-single.html',
#                   {'product': product})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/shop-single.html',
                  {'product': product, 'cart_product_form': cart_product_form})
