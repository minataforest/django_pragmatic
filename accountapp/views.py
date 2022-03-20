from django.shortcuts import render

# Create your views here.


def hello_world(request):
    if request.method == "GET":
        print("dddd")
        return render(request, "accountapp/hello_world.html")
    else:
        return render(request, "accountapp/hello_world.html", context={"text": "text"})
