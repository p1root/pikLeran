from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'generated_by', 'generated_date', 'start_date', 'end_date')
    list_filter = ('report_type', 'generated_date')
    search_fields = ('report_type', 'generated_by__username')
    date_hierarchy = 'generated_date'