from django.db import models

MONTH_CHOICES = (
    ('JAN', 'January'),
    ('FEB', 'February'),
    ('MAR', 'March'),
    ('APR', 'April'),
    ('MAY', 'May'),
    ('JUNE', 'June'),
    ('JULY', 'July'),
    ('AUG', 'August'),
    ('SEP', 'September'),
    ('OCT', 'October'),
    ('NOV', 'November'),
    ('DEC', 'December'),
)

class Month(models.Model):
    month = models.CharField(max_length=10, choices=MONTH_CHOICES)
