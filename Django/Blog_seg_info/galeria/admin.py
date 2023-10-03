from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "link","publicada")
    list_display_links = ("id", "nome", "link")
    search_fields = ("nome",)
    list_filter = ("publicada",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
