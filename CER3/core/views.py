from django.shortcuts import render

def home(request):
    title = "Home"
    data = {
        "title": title,
    }
    return render(request, 'core/home.html', data)