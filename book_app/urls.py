from django.urls import path

from book_app import views

urlpatterns = [
    path('', views.index, name='books index'),
    path('create/', views.create, name='create book'),
    path('edit/<int:pk>', views.edit, name='edit book')

]
