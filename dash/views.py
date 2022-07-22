from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RaspberryInfo


# Create your views here.
def show_dashboard(request):
    data = get_object_or_404(RaspberryInfo, id = 1)
    context = {
        'data': data
    }
    return render(request, 'dash/pruebas.html' , context=context)


@csrf_exempt
def Upload_view(request):

    if request.method == "POST":
        response = {'message: all right'}

        db = RaspberryInfo.objects.get(id = 1)

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


      #  update.time = request.POST.get('time')
        return JsonResponse(list(response), safe=False)

    return HttpResponse("Esta pagina solo sirve para subir info")