from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RunRegister, FailuresList, CategoryList

from django.db.models import Count


def paretodata():
    query = RunRegister.objects.values('failure_id__category__name').filter(status__gt=0) \
        .annotate(minutes=Count('status')).order_by('-minutes')
    categories = []
    categories_min = []
    for element in query:
        categories.append(element['failure_id__category__name'])
        categories_min.append(element['minutes'])
    #print(categories)
    return categories, categories_min


def getuptime(timeline, total_downtime):
    total_time = len(timeline)
    return 100 - int((total_downtime / total_time) * 100)


# Create your views here.
def show_dashboard(request):
    timeline = list(RunRegister.objects.all().values_list('status', flat=True))
    categories, categories_min = paretodata()
    uptime = getuptime(timeline, sum(categories_min))
    context = {
                'categories': categories,
                'categories_min': categories_min,
                'uptime': uptime
               }
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

            timeline = list(RunRegister.objects.all().values_list('status', flat=True))


            categories, categories_min = paretodata()


            # QUERY 2
            query2 = RunRegister.objects.values('failure_id__category__name', 'failure_id__description') \
                .filter(status__gt=0).annotate(minutes=Count('status'))
            description = []
            description_min = []
            for element in query2:
                description.append(element['failure_id__description'])
                description_min.append(element['minutes'])

            uptime = getuptime(timeline, sum(categories_min))

            return JsonResponse({'categories': categories, 'categories_min': categories_min, 'description': description,
                                 'description_min': description_min, 'uptime': uptime})
        return JsonResponse({'status': 'Invalid request'}, status=400)

    return HttpResponse("hola")