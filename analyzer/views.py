from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, "index.html")

def predict(request):
    if request.method == "POST":
        text = request.POST.get("text")

        return JsonResponse({"sentiment": "Testing OK"})
