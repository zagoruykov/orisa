from django.contrib import admin

from .models import Sight, Tag, Price


class PriceInline(admin.TabularInline):
    model = Price
    extra = 0


# Register your models here.
@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    inlines = [
        PriceInline
    ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass
