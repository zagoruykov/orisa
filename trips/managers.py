import logging

from django.db.models import F, Manager, Sum, Q, DecimalField
from django.db.models.functions import Coalesce

logger = logging.getLogger(__name__)


class TripManager(Manager):
    def with_total(self):
        total_cost_for_sights_adults = F('days__day__sight__prices__adult_price') * F('adults')
        total_cost_for_sights_kids = F('days__day__sight__prices__kids_price') * F('kids')
        total_cost_for_sights_free = F('days__day__sight__prices__adult_price') * F('free')
        total = total_cost_for_sights_adults + total_cost_for_sights_kids + total_cost_for_sights_free
        return self.annotate(
            total=total
        )


class DayManager(Manager):
    def with_calculations(self):
        shared = Q(daysight__sight__shared=True)
        not_shared = ~shared
        private_adult_price = Sum(F('daysight__adult_price') * F('daysight__adults_quantity'), filter=not_shared)
        private_extra_price = Sum(F('daysight__adult_price') * F('daysight__extra'), filter=not_shared)
        private_kids_price = Sum(F('daysight__kids_price') * F('trip__kids'), filter=not_shared)
        private_free_price = Sum(F('daysight__adult_price') * F('trip__free'), filter=not_shared)
        shared_price = Coalesce(Sum(F('daysight__adult_price') * F('daysight__adults_quantity'), filter=shared), 0,
                                output_field=DecimalField())
        return self.annotate(
            total_adults=private_adult_price,
            # total_kids=private_kids_price,
            # total_free=private_free_price,
            total_shared=shared_price,
            # total_extra=private_extra_price
        )
