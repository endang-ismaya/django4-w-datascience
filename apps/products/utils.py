import matplotlib.pyplot as plt
import seaborn as sns
import base64

from io import BytesIO
from django.contrib.auth.models import User


def get_salesman_from_id(val):
    salesman = User.objects.get(id=val)
    return salesman


def get_image():
    # create a bytes buffer for the image to save
    buffer = BytesIO()

    # create the plot with the use of BytesIO object as its file
    plt.savefig(buffer, format="png")

    # set the cursor to the beginning of the stream
    buffer.seek(0)

    # retrieve the entire content of the file
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph_utf8 = graph.decode("utf-8")

    # free the memory of the buffer
    buffer.close()

    return graph_utf8


def get_plot(chart_type, *args, **kwargs):
    plt.switch_backend("AGG")

    plt.figure(figsize=(10, 4))
    x = kwargs.get("x")
    y = kwargs.get("y")
    data = kwargs.get("data")

    if chart_type == "bar":
        title = "total price by day (bar)"
        plt.title(title)
        plt.bar(x, y)
    elif chart_type == "line":
        title = "total price by day (line)"
        plt.title(title)
        plt.plot(x, y)
    else:
        title = "Product count"
        plt.title(title)
        sns.countplot(x="name", data=data)

    plt.xticks(rotation=45)
    plt.tight_layout()

    graph = get_image()
    return graph
