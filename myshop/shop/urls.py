from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('shop/', views.product_list, name='shop'),
    path('shop/<slug:category_slug>/', views.product_list, name='category'),
    path('detail/<slug:slug>/', views.product_detail, name='detail'),
    path('detail/<int:id>/<slug:slug>/',
         views.product_detail,
         name='product_detail'),
]
