from django.contrib import admin
from .models import Mensaje


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ["texto", "autor", "fecha"]
    search_fields = ["texto", "autor"]
    list_filter = ["fecha"]
