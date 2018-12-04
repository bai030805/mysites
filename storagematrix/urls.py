from django.urls import path
from . import views

urlpatterns = [
    path('objectstorage/', views.objectstorage_matrix),
    path('objectstorageadd/', views.objectstorage_add),
]
