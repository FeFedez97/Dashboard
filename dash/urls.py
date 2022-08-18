from django.urls import path
from .views import upload_view, show_dashboard,resetdb_view

urlpatterns = [
    path('', show_dashboard, name='Dashboard'),
    path('upload/', upload_view, name='upload_data'),
    path('reset/', resetdb_view, name='reset')
]