from django.contrib import admin
from . models import *
class PersonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Person._meta.fields]
    list_filter = ['Name']
    search_fields = ['Name']
    class Meta:
        model = Person
admin.site.register(Person,PersonAdmin)