from django.urls import path
from .consumers import Test_Consumer

ws_urlpatterns = [
    path('ws/test/', Test_Consumer.as_asgi())
]
