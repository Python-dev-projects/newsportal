from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, '')

def about(request):
    return HttpResponse("<h4>About us page</h4>")


