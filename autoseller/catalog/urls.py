from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:pk>', views.AutoDetailView.as_view(), name='car'),
    path('add_car', views.create, name='add_car'),
    path('<int:pk>/edit_car', views.AutoUpdateView.as_view(), name='edit_car'),
    path('<int:pk>/delete_car', views.AutoDeleteView.as_view(), name='delete_car'),
    path('testdrive/<int:car_id>', views.testdrive, name='testdrive'),
]