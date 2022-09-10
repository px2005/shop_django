from django.urls import path, include, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('shop.urls'), name='shop'),
]
