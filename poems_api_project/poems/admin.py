from django.contrib import admin

# Register your models here.
from .models import  Author,VerseMetric,NoRule,FreePoem,Poem

admin.site.register(VerseMetric)
admin.site.register(NoRule)
admin.site.register(FreePoem)
admin.site.register(Poem)

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
            "id",
            "name",
            "country",
            "date_of_birth",
            "date_of_death"
        ]
    list_filter = [
            "country"
        ]
    search_fields = [
            "name"
    ]
    fieldsets = [
            (None, {"fields": ["name"]}),
            ("Date information", {"fields": ["date_of_birth"]}),
        ]
admin.site.register(Author,AuthorAdmin) 