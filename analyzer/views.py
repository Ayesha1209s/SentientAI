import joblib
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def home(request):
    return render(request, "index.html")

@csrf_exempt
def predict(request):
    if request.method == "POST":
        text = request.POST.get("text")

        text_vec = vectorizer.transform([text])
        prediction = model.predict(text_vec)[0]

        return JsonResponse({"sentiment": prediction})

