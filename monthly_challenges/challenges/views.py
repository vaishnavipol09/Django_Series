from django.shortcuts import render # type: ignore
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore



monthly_challenges_code = {
    "january": "Welcome to January month",
    "february": "Welcome to February month",
    "march": "Welcome to march month",
    "april": "Welcome to april month",
    "may": "Welcome to may month",
    "june": "Welcome to June month",
    "july": "Welcome to July month",
    "august": "Welcome to August month",
    "september": "Welcome to September month",
    "october": "Welcome to October month",
    "november": "Welcome to November month",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges_code.keys())

    return render(request , "/challenges/index.html" , {
        "months" : months

    })

def monthly_challenges_by_integer(request , month):
    months = list(monthly_challenges_code.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge" , args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request , month):
    try:
        challenge_text = monthly_challenges_code[month] 
        return render(request,"challenges/challenge.html", {
            "text": challenge_text ,
            "month_name" : month
        })
    except:
        return HttpResponseNotFound("<h1>This is month is not a valid<h2>")    

           


