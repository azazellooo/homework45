from django.contrib import admin
from webapp.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'date', 'status']
    list_filter = ['date', 'status']
    search_fields = ['description']
    fields = ['id', 'status', 'description', 'date']
    readonly_fields = ['status', 'id']


admin.site.register(Task, TaskAdmin)
# Register your models here.
