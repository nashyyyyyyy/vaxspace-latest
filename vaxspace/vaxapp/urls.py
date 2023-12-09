from django.contrib import admin
from django.urls import path
from . import views

app_name = 'vaxapp'

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('user_register/', views.user_register, name='user_register'),
    path('index/', views.index, name='index'),
    path('index/utilities/', views.utilities, name='utilities'),
    path('healthworker/', views.healthworker, name='healthworker'),
    path('index/barangay/', views.barangay, name='barangay'),
    path('guardian/', views.guardian, name='guardian'),
    path('add_healthworker/', views.add_healthworker, name='add_healthworker'),
    path('index/add_vaccine/', views.add_vaccine, name='add_vaccine'),
    path('guardian/view_record/<int:id>/', views.view_record_guardian, name='view_record_guardian'),
    path('healthworker/view_record/<int:id>/', views.view_record_healthworker, name='view_record_healthworker'),
    path('index/view_record/<int:id>/', views.view_record_admin, name='view_record_admin'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('admin_tables/', views.admin_tables, name='admin_tables'),
    path('buttons/', views.buttons, name='buttons'),
    path('admin_tables/add_record/<int:id>/', views.add_record, name='admin_add_record'),
    path('tables/add_record/<int:id>/', views.add_record, name='add_record'), 
    path('tables/confirmation/<int:id>/', views.confirmation, name='confirmation'),
    path('logout/', views.logout, name='logout'),
]