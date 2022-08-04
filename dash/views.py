from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RunRegister,FailuresList, CategoryList


# Create your views here.
def show_dashboard(request):

    context = {

    }
    return render(request, 'dash/pruebas.html', context=context)


@csrf_exempt
def Upload_view(request):

    if request.method == "POST":
        response = {'message: all right'}

        return JsonResponse(list(response), safe=False)

    # is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    #
    # if is_ajax:
    #     if request.method == 'GET':
    #         rawdata = {'time': db.time,
    #                    'M1B1': db.M1B1, 'M1B2': db.M1B2, 'M1B3': db.M1B3,
    #                    'M2B1': db.M2B1, 'M2B2': db.M2B2, 'M2B3': db.M2B3,
    #                    'M3B1': db.M3B1, 'M3B2': db.M3B2, 'M3B3': db.M3B3,
    #                    }
    #         return JsonResponse(rawdata)
    #     return JsonResponse({'status': 'Invalid request'}, status=400)
