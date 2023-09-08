from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

# Create your views here.
def healthchatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # Use 'message' 
        user_query = data['message']
        # user_query = request.json['message']  # Use 'message' key

        # Make a POST request to the microservice with the user's query
        api_url = "https://health-chat-bot-production.up.railway.app/response"
        response = requests.post(api_url, json={'message': user_query})
        # response.set_cookie('csrftoken', '123456')  
        print(response)

        if response.status_code == 200:
            result_data = response.json()
            response_data = {'response' : result_data}

            response = JsonResponse(response_data)
            response.set_cookie('csrf_token', '123456')
            return response
            # return JsonResponse({'response': result_data})
        else:
            return JsonResponse({'response': "Error: Unable to fetch data from the microservice"})

    return render(request, 'healthchatbot/chatbot1.html')