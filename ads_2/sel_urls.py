from django.urls import path

from ads_2 import views

urlpatterns = [

    path('', views.SelectionListView.as_view()),
    path('<int:pk>/', views.SelectionRetrieveView.as_view()),
    path('<int:pk>/update/', views.SelectionUpdateView.as_view()),
    path('<int:pk>/create/', views.SelectionCreateView.as_view()),
    path('<int:pk>/delete/', views.SelectionDestroyView.as_view()),

]