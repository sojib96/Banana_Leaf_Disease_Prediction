from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .inference_pipeline import InferencePipeline
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import os
import time
# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html', {})
    
class Inference(View):
    @method_decorator(csrf_exempt)
    def post(self, request):
        try:
            overall_start_time = time.time()
            if 'leafImage' not in request.FILES:
                return JsonResponse({'error': 'No image provided'}, status=400)
            
            image = request.FILES['leafImage']
            
            # Save the image temporarily
            temp_image_path = 'temp_image.jpg'
            with open(temp_image_path, 'wb') as temp_image_file:
                for chunk in image.chunks():
                    temp_image_file.write(chunk)
            
            object = InferencePipeline()
            start_time = time.time()
            prediction = object.predict(temp_image_path)
            end_time = time.time()
            Inference_time = (end_time - start_time) 
            Inference_time = "{:.2f}".format(Inference_time)

            os.remove(temp_image_path)

            overall_end_time = time.time()
            over_all_time = (overall_end_time - overall_start_time) 
            over_all_time = "{:.2f}".format(over_all_time)

            return render(request, "inference.html" , {'prediction': prediction, 'Inference_time':Inference_time , 'over_all_time': over_all_time})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)