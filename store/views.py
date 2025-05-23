from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def homepage(request):
    fruits = ['Mango', 'Apple', 'Orange', 'pear']
    return render(request, 'store.html', { fruits })
