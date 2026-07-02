from django.contrib import admin
from django.urls import path, include
from django.template.context_processors import csrf
from django.conf import settings
from django.conf.urls.static import static
from orders import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('shop.urls', 'shop'), namespace='shop')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/create/', views.order_create, name='order_create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
