from django.contrib import admin
from .models import ProjectTracker, DetailsKPI
# Register your models here.
class ModelProjectTracker(admin.ModelAdmin):
    list_display=('name', 'projectId', 'leader', 'status', 'CapEx_Ref', 'sgate_date', 'rgate_date', 'actual_rgate_date', 'week_delay')
    
    def get_queryset(self, request):
        # Fetch the original queryset
        queryset = super().get_queryset(request)
        # If the user is a superuser, return the original queryset
        if request.user.is_superuser:
            return queryset
        # Otherwise, filter the queryset based on the logged-in user's leader
        return queryset.filter(leader=request.user)

admin.site.register(ProjectTracker, ModelProjectTracker)
admin.site.register(DetailsKPI)
