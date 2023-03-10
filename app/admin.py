from django.contrib import admin

from app.models import Service, Agent


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym', 'parent')
    ordering = ('parent', 'name')
    list_filter = ('parent',)
    search_fields = ('name', 'parent__name')


class AgentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'registration_number', 'service', 'role')
    ordering = ('last_name', 'first_name')
    list_filter = ('service',)
    search_fields = ('last_name', 'first_name', 'registration_number')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Agent, AgentAdmin)
