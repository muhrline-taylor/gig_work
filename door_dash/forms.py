from django import forms
from .models import DoorDashStats

WEEKDAY_CHOICES = [
    ('MON', 'Monday'),
    ('TUES', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THURS', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
]

class DDStatsCreateModelForm(forms.ModelForm):
    gas_cost = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    net_pay = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    milage = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    date = forms.DateField()
    other_costs = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    weekday = forms.CharField(max_length=5, required=False, widget=forms.Select(choices=WEEKDAY_CHOICES))

    class Meta:
        model = DoorDashStats
        fields = [
            'gas_cost',
            'net_pay',
            'milage',
            'date',
            'other_costs',
            'weekday'
        ]

class DDStatsCreateForm(forms.Form):
    gas_cost = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    net_pay = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    milage = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}), required=False)
    other_costs = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    weekday = forms.CharField(required=False, widget=forms.Select(choices=WEEKDAY_CHOICES))