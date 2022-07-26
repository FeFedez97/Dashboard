from django.urls import path
from .views import Upload_view, show_dashboard

urlpatterns = [
    path('', show_dashboard, name='Dashboard'),
    path('upload/', Upload_view, name='upload_data'),
]