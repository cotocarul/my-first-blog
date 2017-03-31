from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    return HttpResponse("<h1>Te iubesc, Doamne!Chiar daca Tu nu-mi dai putere!</h1><h3>Bine</h4>")