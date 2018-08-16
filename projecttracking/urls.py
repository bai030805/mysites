from django.urls import path
from . import views

urlpatterns = [
    path('customerlist/', views.customer_list),
    path('customeradd/', views.customer_add),
    path('projectlist/', views.project_list),
    path('projectadd/', views.project_add),
    path('projectactivities/', views.project_activities),
#    path('activitylist/', views.activity_list),
#    path('activityadd/', views.activity_add),
]
