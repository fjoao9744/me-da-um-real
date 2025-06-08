from django.urls import path
from app.views import view

urlpatterns = [
    path('', view),
]
