from django.contrib import admin

from app.models import Service, Agent


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    ordering = ('parent',)


class AgentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'registration_number', 'grade', 'service', 'role')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Agent, AgentAdmin)
