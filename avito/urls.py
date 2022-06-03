from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from avito import settings
from ads import views
from users.views import LocationViewSet

router = routers.SimpleRouter()  # url для ViewSet
router.register('location', LocationViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.root),

    path('cat/', include('ads.cat_urls')),

    path('ad/', include('ads.ad_urls')),

    path('user/', include('users.urls')),

    path('selection/', include('ads.sel_urls')),

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
