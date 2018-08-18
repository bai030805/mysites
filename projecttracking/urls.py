from django.urls import path
from . import views

urlpatterns = [
    path('customerlist/', views.customer_list),
    path('customeradd/', views.customer_add),
    path('customeredit/', views.customer_edit),
    path('projectlist/', views.project_list),
    path('projectadd/', views.project_add),
    path('projectedit/', views.project_edit),
    path('projectactivities/', views.project_activities),
]


