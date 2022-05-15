from django.contrib import admin
from django.urls import path

from ads_2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cat/', views.CategoryView.as_view()),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('ad/', views.AdView.as_view()),
    path('ad/<int:pk>', views.AdDetailView.as_view())
]
