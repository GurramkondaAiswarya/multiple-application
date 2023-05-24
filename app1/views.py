from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_str(request):
    return HttpResponse ('<h1>this is aishu</h1>')
def app1_html(request):
    return render(request, 'app1_string')
