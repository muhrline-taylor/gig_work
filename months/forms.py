from django import forms
from .models import Month

MONTH_CHOICES = [
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
]

class MonthModelForm(forms.ModelForm):
    month = forms.CharField(max_length=5, widget=forms.Select(choices=MONTH_CHOICES))

    class Meta:
        model = Month
        fields = ['month']

class MonthForm(forms.Form):
    month = forms.CharField(widget=forms.Select(choices=MONTH_CHOICES))