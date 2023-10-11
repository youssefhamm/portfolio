from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'read_status')  # Ajoutez 'lu' à la liste d'affichage
    list_filter = ('read_status',)  # Ajoutez un filtre pour les messages lus/non lus
    actions = ['marquer_comme_lu', 'marquer_comme_non_lu']

    def marquer_comme_lu(self, request, queryset):
        queryset.update(read_status=True)
    marquer_comme_lu.short_description = "Marquer les messages sélectionnés comme lus"

    def marquer_comme_non_lu(self, request, queryset):
        queryset.update(read_status=False)
    marquer_comme_non_lu.short_description = "Marquer les messages sélectionnés comme non lus"

admin.site.register(Contact, ContactAdmin)
