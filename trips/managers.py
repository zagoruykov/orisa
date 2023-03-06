from django.db.models import F, Manager


class TripManager(Manager):
    def with_total(self):
        total_cost_for_sights_adults = F('days__day__sight__prices__adult_price') * F('adults')
        total_cost_for_sights_kids = F('days__day__sight__prices__kids_price') * F('kids')
        total_cost_for_sights_free = F('days__day__sight__prices__adult_price') * F('free')
        total = total_cost_for_sights_adults + total_cost_for_sights_kids + total_cost_for_sights_free
        return self.annotate(
            total=total
        )