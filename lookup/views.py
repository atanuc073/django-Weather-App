from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests             # in order to use the url we need to import the json and requests.
    # to externally use requests we need to install via command pip3 install requests
    api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=90869D05-E035-49AC-B552-A6AC9462E868")
    try:
        api=json.loads(api_request.content)

    except Exception as e:
        api="Error..."
# thats how we use external api in our app

    return render(request,'home.html',{'api':api})


def about(request):
    return render(request,'about.html',{})
