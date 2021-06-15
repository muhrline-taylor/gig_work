from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import *
from .models import DoorDashStats
from months.models import Month
from months.forms import MonthForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})

    def post(self, request,*args, **kwargs):
        return redirect('/')

class DoorDashLandingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'door_dash_landing.html', {})

    def post(self, request, *args, **kwargs):
        return redirect('/doorDash')

class DoorDashAllView(View):
    def get(self, request, *args, **kwargs):
        total_milage = 0
        total_gas_cost = 0
        total_other_costs = 0
        total_net_pay = 0
        stats = DoorDashStats.objects.order_by('date')
        for stat in stats:
            if stat.milage != None:
                total_milage += stat.milage
                if stat.net_pay != None:
                    pay_gas_ratio = stat.net_pay / stat.milage
            if stat.gas_cost != None:
                total_gas_cost += stat.gas_cost
            if stat.other_costs != None:
                total_other_costs += stat.other_costs
            if stat.net_pay != None:
                total_net_pay += stat.net_pay
        context = {
            'stats': stats,
            'total_milage': total_milage,
            'total_gas_cost': total_gas_cost,
            'total_other_costs': total_other_costs,
            'total_net_pay': total_net_pay,
        }
        if pay_gas_ratio:
            context['pay_gas_ratio'] = str(round(pay_gas_ratio, 2))
        return render(request, 'door_dash_all.html', context)

    def post(self, request, *args, **kwargs):
        return redirect('/doorDash/all')

class DoorDashMonthView(View):
    def get(self, request, month, *args, **kwargs):
        selected_month = Month.objects.get(month=month.upper())
        stats = DoorDashStats.objects.filter(this_month=selected_month).order_by('date')
        total_milage = 0
        total_gas_cost = 0
        total_other_costs = 0
        total_net_pay = 0
        for stat in stats:
            if stat.milage != None:
                total_milage += stat.milage
            if stat.gas_cost != None:
                total_gas_cost += stat.gas_cost
            if stat.other_costs != None:
                total_other_costs += stat.other_costs
            if stat.net_pay != None:
                total_net_pay += stat.net_pay
        context = {
            'stats': stats,
            'total_milage': total_milage,
            'total_gas_cost': total_gas_cost,
            'total_other_costs': total_other_costs,
            'total_net_pay': total_net_pay,
        }
        return render(request, 'door_dash_month.html', context)

    def post(self, request, month, *args, **kwargs):
        return redirect(f'/doorDash/all/{month}')

class DoorDashOneView(View):
    def get(self, request, id, *args, **kwargs):
        stat = get_object_or_404(DoorDashStats, id=id)
        print(stat.weekday)
        return render(request, 'door_dash_day.html', {'stat':stat})

    def post(self, request, *args, **kwargs):
        return redirect('/doorDash/one')

class DoorDashCreateView(View):
    def get(self, request, *args, **kwargs):
        form = DDStatsCreateForm()
        month_form = MonthForm()
        return render(request, 'door_dash_create.html', {'form': form, 'month_form':month_form})

    def post(self, request, *args, **kwargs):
        form = DDStatsCreateForm(request.POST)
        month_form = MonthForm(request.POST)
        print('**** FORM IS_VALID')
        print(form.is_valid())
        print('*** MONTH_FORM IS VALID')
        print(month_form.is_valid())
        if form.errors:
            context = {'form':form}
            if month_form.errors:
                context['month_form'] = month_form
            return render(request, 'door_dash_create.html', context)
        elif form.is_valid():
            if month_form.is_valid():
                print('**** MONTH_FORM content')
                print(month_form.cleaned_data['month'])
                selected_month = Month.objects.get(month=month_form.cleaned_data['month'])
                DoorDashStats.objects.create(**form.cleaned_data, this_month=selected_month)
            return redirect('/doorDash/all')
        return redirect('/doorDash/new')

class DoorDashWeekdayView(View):
    def get(self, request, weekday, *args, **kwargs):
        print(weekday)
        weekday_stats = DoorDashStats.objects.filter(weekday=weekday.upper())
        total_milage = 0
        total_gas_cost = 0
        total_other_costs = 0
        total_net_pay = 0
        for stat in weekday_stats:
            if stat.milage != None:
                if stat.net_pay != None:
                    total_milage += stat.milage
                    total_net_pay += stat.net_pay
            if stat.gas_cost != None:
                total_gas_cost += stat.gas_cost
            if stat.other_costs != None:
                total_other_costs += stat.other_costs
        context = {
            'total_milage': total_milage,
            'total_gas_cost': total_gas_cost,
            'total_other_costs': total_other_costs,
            'total_net_pay': total_net_pay,
            'weekday_stats': weekday_stats,
        }
        return render(request, 'door_dash_weekday.html', context)

    def post(self, request, *args, **kwargs):
        pass