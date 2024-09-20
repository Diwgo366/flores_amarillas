from django.shortcuts import render

# Create your views here.
def flores(request):
    return render(request, 'flores.html')