from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads import settings
from ads_2 import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.root),

    path('cat/', include('ads_2.cat_urls')),

    path('ad/', include('ads_2.ad_urls')),

    path('user/', include('users.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
