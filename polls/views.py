from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def functiaInPolls(request):

    return HttpResponse("<h1>Din polls: Aleluia, au rasarit rosiile!!!</h1><br>"
                        "<h2>Bine</h2>")