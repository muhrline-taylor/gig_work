from django.db import models
from django.urls import reverse


WEEKDAY_CHOICES = (
    ('MON', 'Monday'),
    ('TUES', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THURS', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
)



class DoorDashStats(models.Model):
    gas_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    net_pay = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    milage = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=False)
    date = models.DateField(max_length=255)
    other_costs = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    weekday = models.CharField(max_length=9, choices=WEEKDAY_CHOICES, default='monday')
    this_month = models.ForeignKey('months.Month', related_name='stat_month', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('door_dash_stats', kwargs={'id':self.id})