from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path("" , views.index),
    path("<int:month>" , views.monthly_challenges_by_integer),
    path("<str:month>" , views.monthly_challenges, name="month_challenge")
]