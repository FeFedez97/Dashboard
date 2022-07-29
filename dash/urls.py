from django.urls import path
from .views import Upload_view, show_dashboard,Test_view

urlpatterns = [
    path('', show_dashboard, name='Dashboard'),
    path('upload/', Upload_view, name='upload_data'),
    path('test/', Test_view, name='test') #delete this after test
]
