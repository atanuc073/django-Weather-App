from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests             # in order to use the url we need to import the json and requests.
    # to externally use requests we need to install via command pip3 install requests

    if request.method == "POST":
        zipcode=request.POST['zipcode']
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=25&API_KEY=90869D05-E035-49AC-B552-A6AC9462E868")
        try:
            api=json.loads(api_request.content)

        except Exception as e:
            api="Error..."
        # thats how we use external api in our app

        if api[0]['Category']['Name'] == "Good":
            category_description="AQI: Good (0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."

        elif api[0]['Category']['Name'] == "Moderate":
            category_description="AQI: Moderate (51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."

        elif api[0]['Category']['Name'] == "USG":
            category_description="AQI: Unhealthy for Sensitive Groups (101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."

        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description="AQI: Unhealthy (151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description="AQI: Very Unhealthy (201 - 300) Health alert: everyone may experience more serious health effects.AQI: Hazardous(301 - 500)"

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description="AQI: Hazardous (301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."

        return render(request,'home.html',{'api':api,'category_description':category_description})
        
        
        

    

    else:

        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=90869D05-E035-49AC-B552-A6AC9462E868")
        try:
            api=json.loads(api_request.content)

        except Exception as e:
            api="Error..."
        # thats how we use external api in our app

        if api[0]['Category']['Name'] == "Good":
            category_description="AQI: Good (0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."

        elif api[0]['Category']['Name'] == "Moderate":
            category_description="AQI: Moderate (51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."

        elif api[0]['Category']['Name'] == "USG":
            category_description="AQI: Unhealthy for Sensitive Groups (101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."

        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description="AQI: Unhealthy (151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description="AQI: Very Unhealthy (201 - 300) Health alert: everyone may experience more serious health effects.AQI: Hazardous(301 - 500)"

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description="AQI: Hazardous (301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."

        return render(request,'home.html',{'api':api,'category_description':category_description})


def about(request):
    return render(request,'about.html',{})
