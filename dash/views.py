import colorsys
import numpy as np
import datetime
import pytz

from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Sum, Max

from .models import RunRegister, FailuresList, CategoryList

from math import ceil, floor


def dateconvertion(dt):
    tz = pytz.timezone(str(timezone.get_current_timezone()))
    return dt.astimezone(tz=tz)


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
  #  timeline = list(RunRegister.objects.all().values_list('status', flat=True))
    linechart = gettimelinechart()
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


def gettimelinechart():
    timeformat = "%H:%M"
    maxbars = 360

    first_register = RunRegister.objects.first()
    last_register = RunRegister.objects.last()

    start_time = dateconvertion(first_register.time_stamp)
    end_time = dateconvertion(last_register.time_stamp)

    if start_time == end_time:
        data = {
            'timelines': [],
            'labels': []
        }

        return data

    dif = end_time-start_time

    minutes = int(ceil(dif.total_seconds()/60))

    step = int(ceil(minutes/maxbars))

    labels = []

    for i in range(0, minutes, step):
        dt = datetime.timedelta(minutes=i)
        temp = start_time + dt
        labels.append(temp.strftime(timeformat))

    query = list(RunRegister.objects.values('status', 'duration'))
    query2 = RunRegister.objects.aggregate(Max('status'))
    num_of_cate = query2['status__max'] + 1
    limit = len(query)

    timelines = np.zeros((num_of_cate, len(labels)))

    current = 0
    remaining_time = query[current]['duration']

    selector = np.zeros(num_of_cate, dtype=float)

    for i in range(len(labels)):

        if int(floor(remaining_time)) < step:
            selector[:] = 0
            selector[query[current]['status']] += remaining_time
            while int(floor(np.sum(selector))+0.0001) < step:
                if current + 1 >= limit:
                    break
                current += 1
                if int(floor(selector.sum() + query[current]['duration'])) < step:
                    selector[query[current]['status']] += query[current]['duration']
                else:
                    residue = round(step - selector.sum(), 2)
                    selector[query[current]['status']] += residue
                    remaining_time = round(query[current]['duration'] - residue, 2)
                    break
            if current == limit:
                cat = query[current-1]['status']
            else:
                cat = selector.argmax()

        else:
            cat = query[current]['status']
            remaining_time -= step

        timelines[cat][i] = 1



    data = {
        'timelines': timelines.tolist(),
        'labels': labels
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


def uptimedata(totaldowntime):
    registers = list(RunRegister.objects.all().values_list('duration', flat=True))
    total = sum(registers)
    if total == 0:
        data = {
            'nums': [],
            'uptime': [],
            'color': []
        }
        return data

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
