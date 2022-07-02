from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # rather its better to pass a dictionary as it is better practice
    return render(request, 'index.html')

def counter(request):
    text = request.GET['text']
    word_count = len(text.split())
    return render(request, 'counter.html', {'amount': word_count})