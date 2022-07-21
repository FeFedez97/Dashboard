from django.urls import path
from .views import get_dashboard_info, show_dashboard

urlpatterns = [
    path('', show_dashboard, name='Dashboard'),
    path('upload/', get_dashboard_info, name='upload_data'),
]