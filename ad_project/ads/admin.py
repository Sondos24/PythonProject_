from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')  # عرض الرابط في لوحة الإدارة
    search_fields = ('title', 'description')
