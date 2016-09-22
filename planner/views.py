from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexx(request):
    return HttpResponse("Here's the text of the Web page.")

def index(request):
    return render(request, 'index.html', {})