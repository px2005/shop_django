from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^cart/', include('cart.urls')),
    re_path(r'^orders/', include('orders.urls')),
    re_path(r'^', include('shop.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
