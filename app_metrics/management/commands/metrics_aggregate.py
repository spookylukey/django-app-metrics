from __future__ import print_function

from django.db import transaction
from django.core.management.base import NoArgsCommand

from app_metrics.models import MetricItem, MetricDay, MetricWeek, MetricMonth, MetricYear

from app_metrics.utils import week_for_date, month_for_date, year_for_date, get_backend


BATCH_SIZE = 100


class Command(NoArgsCommand):
    help = "Aggregate Application Metrics"

    requires_model_validation = True

    def handle_noargs(self, **options):
        """ Aggregate Application Metrics """

        backend = get_backend()

        # If using Mixpanel this command is a NOOP
        if backend == 'app_metrics.backends.mixpanel':
            print("Useless use of metrics_aggregate when using Mixpanel backend")
            return

        # Aggregate Items
        items = MetricItem.objects.all().order_by('id')

        while items.exists():
            with transaction.atomic():
                batch = items[0:BATCH_SIZE]
                for i in batch:
                    # Daily Aggregation
                    day,create = MetricDay.objects.get_or_create(metric=i.metric,
                                                                 created=i.created)

                    day.num = day.num + i.num
                    day.save()

                    # Weekly Aggregation
                    week_date = week_for_date(i.created)
                    week, create = MetricWeek.objects.get_or_create(metric=i.metric,
                                                                    created=week_date)

                    week.num = week.num + i.num
                    week.save()

                    # Monthly Aggregation
                    month_date = month_for_date(i.created)
                    month, create = MetricMonth.objects.get_or_create(metric=i.metric,
                                                                      created=month_date)
                    month.num = month.num + i.num
                    month.save()

                    # Yearly Aggregation
                    year_date = year_for_date(i.created)
                    year, create = MetricYear.objects.get_or_create(metric=i.metric,
                                                                    created=year_date)
                    year.num = year.num + i.num
                    year.save()

                # Kill off our items
                items.filter(id__in=[i.id for i in batch]).delete()
