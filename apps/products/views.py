from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "products/index.html", context)
