import requests

API_KEY = "a7342feeb4msh25abe0aad58e0f8p1995e1jsne02c951571ab"
API_HOST = "tennis-live-data.p.rapidapi.com"

url = "https://tennis-live-data.p.rapidapi.com/tournaments/ATP/2020"

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": API_HOST
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Live Tennis Data:")
    print(data)
else:
    print("Failed to fetch data:", response.status_code)
