from django.contrib import admin
from . models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Person._meta.fields]
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Person


admin.site.register(Person,PersonAdmin)