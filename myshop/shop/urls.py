from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('shop/', views.product_list, name='shop'),
    path('shop/<slug:category_slug>/', views.product_list, name='category'),
    path('detail/<slug:slug>/', views.product_detail, name='detail'),
#     path(r'^(?P<category_slug>[-\w]+)/$',
#         views.product_list,
#         name='product_list_by_category'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]
