from decimal import Decimal
from functools import reduce

import nested_admin
from django.contrib import admin

from .models import Trip, Day, DaySight
from .services import archive_program


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
        ('Profit', {
            'fields': ('commission', 'profit',)
        }),
        ('Expenses (Read-only)', {
            'classes': ('collapse',),
            'fields': ('total_price', 'total_per_person_price'),
        }),
    )

    readonly_fields = ('total_price', 'total_per_person_price')

    list_display = ('title', 'client', 'group', 'total_price', 'total_per_person_price', )


    def __get_day_with_calculations(self):
        return Day.objects.with_calculations().filter(trip=self)

    @admin.display(description='Total price')
    def total_price(self, obj: Trip):
        total = Decimal('0.00')
        for day in Day.objects.with_calculations().filter(trip=obj).all():
            vehicles = day.vehiclestrips_set.all()
            vehicles_price = reduce(lambda acc, curr: acc + curr.price * curr.quantity, vehicles, Decimal('0.00'))
            guides = day.guidetrips_set.all()
            guides_price = reduce(lambda acc, curr: acc + curr.price * curr.quantity, guides, Decimal('0.00'))
            total_per_day = vehicles_price + guides_price + day.total_adults + day.total_shared
            total += total_per_day
        return total

    #
    @admin.display(description='Price per person')
    def total_per_person_price(self, obj: Trip):
        per_person = Decimal('0.00')
        for day in Day.objects.with_calculations().filter(trip=obj).all():
            vehicles = day.vehiclestrips_set.all()
            vehicles_price = reduce(lambda acc, curr: acc + curr.price * curr.quantity, vehicles, Decimal('0.00'))
            guides = day.guidetrips_set.all()
            guides_price = reduce(lambda acc, curr: acc + curr.price * curr.quantity, guides, Decimal('0.00'))
            day_per_person = (vehicles_price + guides_price + day.total_adults + day.total_shared) / day.trip.adults
            per_person += day_per_person
        return per_person

    @admin.action(description='Generate program')
    def generate_program(self, request, queryset):
        return archive_program(queryset)
    # @admin.action(description='Generate program')
    # def generate_program(self, request, queryset):
    #     for trip in queryset:
    #         trip.generate_program()
    #     # return archive_program
    #     return trip.generate_program()

    actions = [generate_program]

@admin.register(Day)
class DayAdmin(nested_admin.NestedModelAdmin):
    pass
