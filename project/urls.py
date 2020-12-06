from django.urls import path
from barbearia.views import home, form, create, view, delete, edit

urlpatterns = [
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('edit/<int:pk>/', edit, name='edit')
]