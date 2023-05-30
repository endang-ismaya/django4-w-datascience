from django.shortcuts import render


def upload_file(request):
    context = {}
    return render(request, "csvs/csv-upload.html", context)
