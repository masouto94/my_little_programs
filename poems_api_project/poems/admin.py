from django.contrib import admin

# Register your models here.
from .models import  Author,VerseMetric,StropheMetric,NoRule,Poem,PoemType

admin.site.register(VerseMetric)
admin.site.register(PoemType)
admin.site.register(StropheMetric)
admin.site.register(NoRule)
# admin.site.register(FreePoem)
# admin.site.register(Sonnet)

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
    
class PoemAdmin(admin.ModelAdmin):
    list_display = [
            "id",
            "title",
            "author",
            "get_poem_types"
        ]
    list_filter = [
            "title",
            "author",
            "poem_type"
        ]
    search_fields = [
            "title",
    ]

    
admin.site.register(Poem,PoemAdmin) 
admin.site.register(Author,AuthorAdmin) 