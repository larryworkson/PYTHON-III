import requests
key = ''
response = requests.get(f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={key}')
print(response.json())