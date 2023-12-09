
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee', views.employeeListView),
    path('api/employee/<int:pk>', views.employeeDetailView),
    path('api/users', views.UserListView),
    
    
]
