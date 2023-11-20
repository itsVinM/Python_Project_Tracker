from django.contrib import admin
from django.urls import path
from tracker.views import project_tracker, about_view, project_info, overall_gantt_chart

urlpatterns = [
    path('', project_tracker, name='project_tracker'),
    path('admin/', admin.site.urls),
    path('project_info/<int:pk>/', project_info, name='project_info'),
    path('about.html/', about_view, name='about'),
    path('gantt.html/', overall_gantt_chart, name='gantt')
   
]
