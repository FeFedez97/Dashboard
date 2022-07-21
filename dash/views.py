from django.shortcuts import render


# Create your views here.
def show_dashboard(request):

    return render(request, 'dash/pruebas.html')

def get_dashboard_info(request):
    if request.method == 'POST':
        print(request.get('ex'))

    return render(request, 'dash/Upload_page.html')
