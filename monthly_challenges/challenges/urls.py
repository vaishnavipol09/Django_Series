from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("january" , views.index)
]