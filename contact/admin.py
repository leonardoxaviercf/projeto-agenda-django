from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',)
    ordering = ('id',) # Colocando um -id altera a ordem para decrescente
    # list_filter = ('created_date',)
    search_fields = ('id', 'first_name', 'last_name',)
    list_per_page = (15)
    list_max_show_all = (200)
    # list_editable = ('first_name', 'last_name',) Posso editar diretamente pela aba inicial do admin, sem precisar entrar no contato
    list_display_links = ('id', 'phone',)