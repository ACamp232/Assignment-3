
import urllib.request
import urllib.parse
import json
from pprint import pprint

MAPQUEST_API_KEY = 'RtrjmrcuCbiG25nSkQEGVxG4qNlBGmGE'
MBTA_key = '65cc3ac45cde4504a04a945a40688211'


def get_latlong_coordinates(url): 
    """extract the latitude and longitude from the JSON response data and returns the longitude and latitude as a tuple"""
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    latitude = response_data['results'][0]['locations'][0]['latLng']['lat']
    longitude = response_data['results'][0]['locations'][0]['latLng']['lng']
    my_list = (latitude, longitude)
    print (my_list)
    # return latitude and longitude
    #how to store both together in a tuple or list 
    # change function to work with url function 


def make_url(address):
    """function that takes an address or place name as input and returns a properly encoded URL to make a MapQuest geocode request"""
    address = input()
    # user_param = urllib.parse.urlencode(address)
    # user_param = user_param.encode('ascii')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={address}'
    url = url.replace(' ', '%2f')
    return url
    # with urllib.request.urlopen(url) as f:
        # url = f.read().decode('utf-8')


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    
    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_key}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    # print (url)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    place_name = input()
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    url = url.replace(' ', '%2f')
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    latitude = response_data['results'][0]['locations'][0]['latLng']['lat']
    longitude = response_data['results'][0]['locations'][0]['latLng']['lng']
    stop_url = f'https://api-v3.mbta.com/stops?api_key={MBTA_key}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    j = urllib.request.urlopen(stop_url)
    response_text = j.read().decode('utf-8')
    response_data = json.loads(response_text)
    stop = response_data['main']


# def main():
#     get_nearest_station(latitude = 42.29822, longitude = -71.26543)
#     find_stop_near('babson college')
#     get_latlong_coordinates(url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College')



# # if __name__ == "__main__":
# #     main()
