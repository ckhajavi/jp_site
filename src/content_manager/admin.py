from .models import Description, DescriptionImage
from django.contrib import admin

class DescriptionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    class Meta:
        model = Description

        
admin.site.register(Description, DescriptionAdmin)
admin.site.register(DescriptionImage)
# Register your models here.
