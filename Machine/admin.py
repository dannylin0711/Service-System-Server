from django.contrib import admin

# Register your models here.
from .models import Machine, Errorcode, AdditionalFile


class MachineAdmin(admin.ModelAdmin):
    list_display = ('machine_type',)
    ordering = ('machine_type',)
    search_field = ('machine_type',)


class ErrorcodeAdmin(admin.ModelAdmin):
    list_display = ('code_name','machine_type','description')
    ordering = ('machine_type',)
    search_field = ('machine_type',)

class AdditionalFileAdmin(admin.ModelAdmin):
    list_display = ('file_name',)
    ordering = ('file_name',)
    search_field = ('file_name',)

admin.site.register(Machine, MachineAdmin)
admin.site.register(Errorcode, ErrorcodeAdmin)
admin.site.register(AdditionalFile)
