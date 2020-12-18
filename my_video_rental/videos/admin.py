from django.contrib import admin

# Register your models here.
from . import models


class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']  # Ordering Fields for detail view

    search_fields = ['title', 'length']  # Adding search

    list_filter = ['release_year', 'length', 'title']  # Adding Filters

    list_display = ['title', 'release_year', 'length']  # Adding Fields for list view

    list_editable = ['length']  # Editable list view


admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)  # Register customize MovieAdmin class
