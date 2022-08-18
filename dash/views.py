import colorsys
import numpy as np
import datetime
import pytz

from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RunRegister, FailuresList, CategoryList

from django.db.models import Count, Sum


def resestdb():
    linespeed = 60
    RunRegister.objects.all().delete()
    failure = FailuresList.objects.get(id=1)
    timestamp = datetime.datetime.now()
    newRegister = RunRegister(time_stamp=timestamp, failure_id=failure, line_speed=linespeed, bottle_count=0,
                              bottle_rejections=0)
    newRegister.save()

def colormap(level):

    max = 225
    step = int(max/50)

    if level <= 50:
        r = max
        g = level*step
    else:
        g = max
        r = max + (-step)*(level-50)

    b = 0
    color = f'rgb({r},{g},{b})'
    return [color, '#D9D9D9']

def getValues():
    timeline = list(RunRegister.objects.all().values_list('status', flat=True))
    linechart = gettimelinechart(timeline)
    pareto = paretodata()
    uptime = uptimedata(sum(pareto['minutes']))
    pie = piedata()

    values = {
        'pareto': pareto,
        'pie': pie,
        'uptime': uptime,
        'timeline': linechart
    }

    return values


def gettimelinechart(timeline):
    num_of_categories = max(timeline) + 1
    lenght = len(timeline)
    timelines = np.zeros((num_of_categories, lenght), dtype=int)
    for count, state in enumerate(timeline):
        timelines[state][count] = 1

    data = {
        'timelines': timelines.tolist()
    }

    return data


def paretodata():
    query = RunRegister.objects.values('failure_id__category__name').filter(status__gt=0) \
        .annotate(minutes=Sum('duration')).order_by('-minutes')
    categories = []
    categories_min = []
    for element in query:
        categories.append(element['failure_id__category__name'])
        categories_min.append(element['minutes'])

    data = {
        'labels': categories,
        'minutes': categories_min,
    }
    return data


def piedata():
    colors = ['#e6194B', '#3cb44b', '#e6c700', '#4363d8', '#f58231', '#911eb4', '#42d4f4', '#f032e6', '#bfef45',
              '#fabed4', '#469990', '#dcbeff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1',
              '#000075']

    query = RunRegister.objects.values('failure_id__category__name', 'failure_id__description') \
        .filter(status__gt=0).annotate(minutes=Sum('duration'))
    description = []
    description_min = []
    machine = []
    machine_min = []
    failure_colors = []
    machine_colors = []

    for element in query:

        if not element['failure_id__category__name'] in machine:
            machine.append(element['failure_id__category__name'])
            machine_min.append(0)
            i = len(machine_colors)
            if i <= len(colors[i]):
                machine_colors.append(colors[i])

        if len(machine_colors) <= len(colors):
            failure_colors.append(machine_colors[-1])
        machine_min[-1] += element['minutes']
        description.append(element['failure_id__description'])
        description_min.append(element['minutes'])

    data = {
        'machines_labels': machine,
        'machines_times': machine_min,
        'machines_colors': machine_colors,
        'failures_labels': description,
        'failures_times': description_min,
        'failures_colors': failure_colors
    }

    return data


def dateconvertion(dt):
    tz = pytz.timezone(str(timezone.get_current_timezone()))
    return dt.astimezone(tz=tz)



def uptimedata(totaldowntime):
    registers = list(RunRegister.objects.all().values_list('duration', flat=True))
    total = sum(registers)
    downtime = round(totaldowntime/total, 2)
    uptime = round(1-downtime, 2)
    intuptime = int(uptime*100)
    color = colormap(intuptime)
    data = {
        'nums': [uptime, downtime],
        'uptime': intuptime,
        'color': color
    }
    return data

###################################################################################################################
# Create your views here.
def show_dashboard(request):
    context = getValues()
    return render(request, 'dash/dashboard.html', context=context)


@csrf_exempt
def upload_view(request):
    if request.method == "POST":
        response = {'message: all right'}
        lastregister = RunRegister.objects.last()
        timestr = request.POST.get("time_stamp")
        currenttime = datetime.datetime.fromisoformat(timestr)
        lastregister_time = dateconvertion(lastregister.time_stamp)
        timedif = currenttime - lastregister_time
        duration = round(timedif.total_seconds() / 60, 2)
        lastregister.duration = duration
        lastregister.save()

        failure = FailuresList.objects.get(id=request.POST.get("failure_id"))

        newregister = RunRegister \
                (
                time_stamp=currenttime,
                status=request.POST.get("status"),
                failure_id=failure,
                duration=0.0,
                line_speed=request.POST.get("line_speed"),
                bottle_count=request.POST.get("bottle_count"),
                bottle_rejections=request.POST.get("bottle_rejections")
            )
        newregister.save()

        return JsonResponse(list(response), safe=False)

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            return JsonResponse(getValues())

        return JsonResponse({'status': 'Invalid request'}, status=400)


def resetdb_view(request):
    resestdb()
    return redirect('Dashboard')
