from django.contrib import admin
from django.urls import path
from tracker import views 

urlpatterns = [
    path('', views.project_tracker, name='project_tracker'),
    path('admin/', admin.site.urls),
    path('project_info/<int:pk>/', views.project_info, name='project_info'),
    path('gantt.html/', views.overall_gantt_chart, name='gantt'), 
    path('about.html/', views.about_view, name='about'),
]
