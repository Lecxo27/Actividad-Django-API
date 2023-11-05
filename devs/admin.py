from django.contrib import admin
from devs.models import Dev
# Register your models here.
@admin.register(Dev)
class DevAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_at']
