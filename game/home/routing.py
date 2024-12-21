from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path("ws/game/<code>", gaming.as_asgi()),
]