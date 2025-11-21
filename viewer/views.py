from django.shortcuts import render

def home(request):
    # You can pass data (e.g., scene list) here if you want
    return render(request, 'home.html', {})
