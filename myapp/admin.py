from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import State, Staff, Lake


@admin.register(State)
class StateAdmin(gis_admin.GISModelAdmin):
    list_display = ('name', 'population')
    list_filter = ('population',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex', 'salary', 'state')
    list_filter = ('sex', 'state', 'age')
    search_fields = ('name', 'address')
    list_editable = ('salary',)
    ordering = ('name',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'age', 'sex', 'address')
        }),
        ('Employment Details', {
            'fields': ('salary', 'state')
        }),
    )


@admin.register(Lake)
class LakeAdmin(gis_admin.GISModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
