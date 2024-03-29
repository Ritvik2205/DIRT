from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.serializers import serialize
# from .source.openai_api import generate_image 
from .prompts import image_generator
from .prompts import question_generator
from openai import OpenAI

# client = OpenAI()
# openai.api_key = settings.OPENAI_API_KEY



# def test_func(request, prom)


@api_view(['POST'])
def generate_image(request):

    if request.method == 'POST':
        # try:
        #     # Make a request to OpenAI API to generate an image
        #     response = client.images.generate(prompt="A pixelart image of a grocery store with a French shopper",
        #     n=1,
        #     size="1024x1024")
        #     print("created response:", response)
        #     image_url = response

        # except Exception as e:
        #     print(f"An error occurred: {e}")

        # image_url = "potato"
        # image_url = generate_image("A pixelart image of a grocery store with a French shopper")
        # print(request)
        # prompt = request.data['prompt']
        image_url = image_generator(0, 0)
        print(image_url)
        data = {"url": image_url}
        return JsonResponse(data)


@api_view(['POST'])
def generate_question(request):

    if request.method == 'POST':
        # ethnicity_idx = request.data['ethnicity_idx']
        ethnicity_idx = 0
        question = question_generator(ethnicity_idx)
        data = {"question": question}
        return JsonResponse(data)