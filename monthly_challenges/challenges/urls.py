from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("<int:month>" , views.monthly_challenges_by_integer),
    path("<str:month>" , views.monthly_challenges)
]