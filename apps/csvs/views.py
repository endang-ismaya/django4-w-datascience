import csv
from django.shortcuts import render
from django.contrib.auth.models import User

from apps.csvs.forms import CsvForm
from apps.csvs.models import Csv
from apps.products.models import Product, Purchase


def upload_file(request):
    error_message = None
    success_message = None

    form = CsvForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = CsvForm()

        try:
            obj = Csv.objects.get(activated=False)

            with open(obj.file_name.path, "r") as f:
                reader = csv.reader(f)

                for row in reader:
                    row = "".join(row)
                    row = row.split(";")
                    user = User.objects.get(id=row[3])
                    prod, created = Product.objects.get_or_create(name=row[0])

                    Purchase.objects.create(
                        product=prod,
                        price=int(row[2]),
                        quantity=int(row[1]),
                        salesman=user,
                        created_at=row[4] + " " + row[5],
                    )

            obj.activated = True
            obj.save()

            success_message = "Uploaded successfully."
        except Exception:
            error_message = "Something went wrong..."

    context = {
        "form": form,
        "error_message": error_message,
        "success_message": success_message,
    }
    return render(request, "csvs/csv-upload.html", context)
