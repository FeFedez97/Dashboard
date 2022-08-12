from django.urls import path
from .views import upload_view, show_dashboard

urlpatterns = [
    path('', show_dashboard, name='Dashboard'),
    path('upload/', upload_view, name='upload_data'),
]