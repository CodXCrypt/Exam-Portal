from django.shortcuts import render


def LandingPage(request):
    return render(request, "frontend/index.html")
