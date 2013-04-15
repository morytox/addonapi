from django.contrib import admin
from models import Addon

class AddonAdmin(admin.ModelAdmin):
	date_hirarchy = "created_at"
	fields = ("name", "config_vars")
	list_display = ["name", "config_vars", "date_modified"]
	list_display_links = ["name"]
	list_filter = ["name", "date_modified"]
	search_fields = ["name", "config_vars"]

admin.site.register(Addon, AddonAdmin)