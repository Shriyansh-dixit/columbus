import requests

# Replace these with your API keys
google_api_key = 'AIzaSyCsaCJDIYvuDWqXXj0n2i2BqUb71HoAPr4'

def get_hotels(city):
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': f'best hotels in {city}',
        'key': google_api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract and return relevant hotel data
    return data.get('results', [5])

def get_places_to_visit(city):
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': f'places to visit in {city}',
        'key': google_api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract and return relevant place data
    return data.get('results', [5])

def get_restaurants(city):
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': f'restaurants in {city}',
        'key': google_api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract and return relevant restaurant data
    return data.get('results', [5])

if __name__ == "__main__":
    city = input("Enter the city: ")

    hotels = get_hotels(city)
    places_to_visit = get_places_to_visit(city)
    restaurants = get_restaurants(city)

    # Display the retrieved data 
    print("Best Hotels:")
    for hotel in hotels:
        print(hotel['name'])

    print("\nPlaces to Visit:")
    for place in places_to_visit:
        print(place['name'])

    print("\nRestaurants:")
    for restaurant in restaurants:
        print(restaurant['name'])
