from django.contrib import admin

# Register your models here.
from .models import Document

#admin.site.register(Document)

#define the admin class
@admin.register(Document)
class DocAdmin(admin.ModelAdmin):
	list_display=(id,'description','typedoc','uploaded_at')

#Register the admin Class with the associate model
#admin.site.register(Document,DocAdmin)