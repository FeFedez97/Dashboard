from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RunRegister, FailuresList, CategoryList

from django.db.models import Count, Sum


def getValues():
    timeline = list(RunRegister.objects.all().values_list('status', flat=True))
    pareto = paretodata()
    uptime = uptimedata(timeline, sum(pareto['minutes']))
    pie = piedata()

    values = {
        'pareto': pareto,
        'pie': pie,
        'uptime': uptime
    }

    return values

def paretodata():
    query = RunRegister.objects.values('failure_id__category__name').filter(status__gt=0) \
        .annotate(minutes=Count('status')).order_by('-minutes')
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
        .filter(status__gt=0).annotate(minutes=Count('status'))
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

###################################################################################################################
def uptimedata(timeline, total_downtime):
    total_time = len(timeline)
    return 100 - int((total_downtime / total_time) * 100)


# Create your views here.
def show_dashboard(request):
    context = getValues()
    return render(request, 'dash/dashboard.html', context=context)


@csrf_exempt
def upload_view(request):
    if request.method == "POST":
        response = {'message: all right'}

        failure = FailuresList.objects.get(id=request.POST.get("failure_id"))
        register = RunRegister(status=request.POST.get("status"), failure_id=failure)
        register.save()

        return JsonResponse(list(response), safe=False)

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            return JsonResponse(getValues())

        return JsonResponse({'status': 'Invalid request'}, status=400)