from django.contrib import admin

from app.models import Service, Agent


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym', 'parent')
    ordering = ('parent', 'name')


class AgentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'registration_number', 'grade', 'service', 'role')
    ordering = ('last_name', 'first_name')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Agent, AgentAdmin)
