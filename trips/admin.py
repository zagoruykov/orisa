import nested_admin
from django.contrib import admin

from .models import Trip, Day, DaySight, VehiclesTrips


class SightsInline(nested_admin.NestedStackedInline):
    model = DaySight
    extra = 0
    classes = ['collapse']


class GuideInline(nested_admin.NestedTabularInline):
    model = Day.guides.through
    extra = 1
    classes = ['collapse']

class VehiclesInline(nested_admin.NestedTabularInline):
    model = Day.vehicles.through
    extra = 1
    classes = ['collapse']


class DaysInline(nested_admin.NestedTabularInline):
    model = Day
    extra = 0
    inlines = [
        VehiclesInline,
        GuideInline,
        SightsInline,
    ]


@admin.register(DaySight)
class DaySightAdmin(admin.ModelAdmin):
    pass


# Register your models here.
# @admin.register(Trip)
# class TripAdmin(nested_admin.NestedModelAdmin):
#     pass


@admin.register(Trip)
class TripAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        DaysInline
    ]

    fieldsets = (
        ('General', {
            'fields': ('title', 'description', 'client',)
        }),
        ('Group', {
            'fields': ('adults', 'kids', 'free',)
        }),
        # ('Additional services', {
        #     'fields': ('vehicles',)
        # }),
        ('Profit', {
            'fields': ('commission', 'profit',)
        }),
        # ('Expenses (Read-only)', {
        #     'classes': ('collapse',),
        #     'fields': ('total_price', 'total_per_person_price'),
        # }),
    )


#     readonly_fields = ('total_price', 'total_per_person_price')
#
#     list_display = ('title', 'client', 'group', 'total_price', 'total_per_person_price', 'trip_start_at', 'trip_end_at')
#
#     actions = ('generate_program',)
#
#     @admin.display(description='Group')
#     def group(self, obj: Trip):
#         return obj.group()
#
#     @admin.display(description='Date start')
#     def trip_start_at(self, obj: Trip):
#         return obj.trip_start_at()
#
#     @admin.display(description='Date end')
#     def trip_end_at(self, obj: Trip):
#         return obj.trip_end_at()
#
#     @admin.display(description='Total price')
#     def total_price(self, obj: Trip):
#         return obj.calculate_total()
#
#     @admin.display(description='Price per person')
#     def total_per_person_price(self, obj: Trip):
#         return obj.calculate_per_person()
#
#     @admin.action(description='Generate program')
#     def generate_program(self, request, queryset):
#         for trip in queryset:
#             trip.generate_program()


@admin.register(Day)
class DayAdmin(nested_admin.NestedModelAdmin):
    pass
