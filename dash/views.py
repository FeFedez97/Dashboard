from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RaspberryInfo


# Create your views here.
def show_dashboard(request):
    data = get_object_or_404(RaspberryInfo, id=1)
    Machine_times = data.getmachinetimes()
    context = {
        'data': data,
        'machine_times': Machine_times
    }
    return render(request, 'dash/pruebas.html', context=context)


@csrf_exempt
def Upload_view(request):
    db = RaspberryInfo.objects.get(id=1)

    if request.method == "POST":
        response = {'message: all right'}

        db.time = request.POST.get('time')
        db.M1B1 = request.POST.get('M1B1')
        db.M1B2 = request.POST.get('M1B2')
        db.M1B3 = request.POST.get('M1B3')
        db.M2B1 = request.POST.get('M2B1')
        db.M2B2 = request.POST.get('M2B2')
        db.M2B3 = request.POST.get('M2B3')
        db.M3B1 = request.POST.get('M3B1')
        db.M3B2 = request.POST.get('M3B2')
        db.M3B3 = request.POST.get('M3B3')
        db.save()

        return JsonResponse(list(response), safe=False)

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            rawdata = {'time': db.time,
                       'M1B1': db.M1B1, 'M1B2': db.M1B2, 'M1B3': db.M1B3,
                       'M2B1': db.M2B1, 'M2B2': db.M2B2, 'M2B3': db.M2B3,
                       'M3B1': db.M3B1, 'M3B2': db.M3B2, 'M3B3': db.M3B3,
                       }
            return JsonResponse(rawdata)
        return JsonResponse({'status': 'Invalid request'}, status=400)
