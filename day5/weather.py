import requests

print("Lets build ismple weather application")

location = input("Location :")
date = input("Date (YYYY-MM-DD):")

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date}"


response = requests.get(url, params={'key':"HCU2HJXB7N2U8K26NM4E4W5GE"})

data = response.json()

print(data)
print(f"The weather of {location} on the date {date} is : {data['description']}") 
