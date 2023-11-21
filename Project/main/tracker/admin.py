from django.contrib import admin
from .models import ProjectTracker, DetailsKPI
# Register your models here.


class ModelProjectTracker(admin.ModelAdmin):
    list_display=('name', 'projectId', 'leader', 'status', 'CapEx_Ref', 'sgate_date', 'rgate_date', 'actual_rgate_date', 'week_delay')

admin.site.register(ProjectTracker, ModelProjectTracker)
admin.site.register(DetailsKPI)
