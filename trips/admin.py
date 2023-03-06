import nested_admin
from django.contrib import admin

from sights.models import Sight
from .models import Trip, Day


class SightsInline(nested_admin.NestedStackedInline):
    model = Sight


class DaysInline(nested_admin.NestedTabularInline):
    model = Trip.days.through
    extra = 1
    inlines = [
        # SightsInline
    ]


class GuideInline(nested_admin.NestedTabularInline):
    model = Trip.guide.through
    extra = 1


# Register your models here.
@admin.register(Trip)
class TripAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        GuideInline,
        DaysInline
    ]

    fieldsets = (
        ('General', {
            'fields': ('title', 'description', 'client',)
        }),
        ('Group', {
            'fields': ('adults', 'kids', 'free',)
        }),
        ('Additional services', {
            'fields': ('vehicle',)
        }),
        ('Profit', {
            'fields': ('commission', 'profit',)
        }),
        ('Expenses (Read-only)', {
            'classes': ('collapse',),
            'fields': ('total_price', 'total_per_person_price'),
        }),
    )
    readonly_fields = ('total_price', 'total_per_person_price')

    list_display = ('title', 'client', 'group', 'total_price', 'total_per_person_price', 'trip_start_at', 'trip_end_at')

    actions = ('generate_program',)

    @admin.display(description='Group')
    def group(self, obj: Trip):
        return obj.group()

    @admin.display(description='Date start')
    def trip_start_at(self, obj: Trip):
        return obj.trip_start_at()

    @admin.display(description='Date end')
    def trip_end_at(self, obj: Trip):
        return obj.trip_end_at()

    @admin.display(description='Total price')
    def total_price(self, obj: Trip):
        return obj.calculate_total()

    @admin.display(description='Price per person')
    def total_per_person_price(self, obj: Trip):
        return obj.calculate_per_person()

    @admin.action(description='Generate program')
    def generate_program(self, request, queryset):
        for trip in queryset:
            trip.generate_program()


@admin.register(Day)
class DayAdmin(nested_admin.NestedModelAdmin):
    pass
