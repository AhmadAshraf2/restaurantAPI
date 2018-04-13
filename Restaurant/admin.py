from django.contrib import admin
from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'opens_at', 'closes_at')
    list_filter = ('name',)


admin.site.register(Restaurant, RestaurantAdmin)
