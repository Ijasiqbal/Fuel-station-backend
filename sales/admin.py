from django.contrib import admin
from .models import Sales, ClosingSales

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'fuelSales', 'totalCash', 'totalCard', 'totalPaytm', 'credit', 'shortage')
    list_filter = ('date',)
    search_fields = ('date',)
    date_hierarchy = 'date'
    ordering = ('-date', '-time')
    fieldsets = (
        ('Sales Information', {
            'fields': ('fuelSales', 'extraGreenSales', 'dieselSales', 'petrolSales', 'extraPremiumSales', 'oil', 'itemSales')
        }),
        ('Financial Details', {
            'fields': ('openingBalance', 'totalCash', 'totalCard', 'totalPaytm', 'credit', 'closingBalance', 'shortage')
        }),
        ('Date and Time', {
            'fields': ('date', 'time')
        }),
    )

@admin.register(ClosingSales)
class ClosingSalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Du1Nozzle1', 'Du1Nozzle2', 'Du2Nozzle1', 'Du2Nozzle2')
    fieldsets = (
        ('Dispensing Unit 1', {
            'fields': ('Du1Nozzle1', 'Du1Nozzle2', 'Du1Nozzle3', 'Du1Nozzle4')
        }),
        ('Dispensing Unit 2', {
            'fields': ('Du2Nozzle1', 'Du2Nozzle2', 'Du2Nozzle3', 'Du2Nozzle4')
        }),
        ('Dispensing Unit 3', {
            'fields': ('Du3Nozzle1', 'Du3Nozzle2', 'Du3Nozzle3', 'Du3Nozzle4')
        }),
        ('Dispensing Unit 4', {
            'fields': ('Du4Nozzle1', 'Du4Nozzle2', 'Du4Nozzle3', 'Du4Nozzle4')
        }),
    )
