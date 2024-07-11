from django.shortcuts import render # type: ignore
from django.http import HttpResponse , HttpResponseNotFound # type: ignore

# Create your views here.

def monthly_challenges_by_integer(request , month):
    return HttpResponse(month)

def monthly_challenges(request , month):
    challenge_text = None
    if month == "january":
        challenge_text = "Welcome to January month"
    elif month == "february":
        challenge_text = "Welcome to February month"    
    elif month == "march":
        challenge_text = "Welcome to march month"    
    elif month == "april":
        challenge_text = "Welcome to april month"    
    elif month == "may":
        challenge_text = "Welcome to may month" 
    else:
        return HttpResponseNotFound("Month not found")    

    return HttpResponse(challenge_text)           


