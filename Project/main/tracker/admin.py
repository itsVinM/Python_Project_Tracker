from django.contrib import admin
from .models import ProjectTracker
# Register your models here.


class ModelProjectTracker(admin.ModelAdmin):
    list_display=('name', 'leader', 'status', 'sgate_date', 'rgate_date', 'actual_rgate_date', 'week_delay')

admin.site.register(ProjectTracker, ModelProjectTracker)


