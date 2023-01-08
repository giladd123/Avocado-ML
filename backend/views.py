from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from rest_framework.parsers import JSONParser
from .serializers import InputSerializer
from django.views.decorators.csrf import csrf_exempt
import io
from .predict import get_prediciton
# Create your views here.

@csrf_exempt
def calculate_price(request):
    if request.method == "POST":
        print(request.body.decode("utf-8"))
        stream = io.BytesIO(request.body)
        data = JSONParser().parse(stream=stream)
        serializer = InputSerializer(data=data)

        if not serializer.is_valid():
            return HttpResponseBadRequest("Bad data")
        
        input = serializer.validated_data
        
        ans = get_prediciton(input)
        
        return HttpResponse(ans)
    
    return HttpResponseNotAllowed(["POST"])