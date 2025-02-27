from datetime import datetime as dt, timedelta as td
from pprint import pprint
import requests

top_destinations = [
    # {"gua": [("mia", 10), ("lax", 10), ("bos", 10)]},
    {"GUA": [("MIA", 10)]},
    # {"sal": [("nyc", 10), ("lax", 10), ("fll", 10)]}
]

servers = "https://api.tequila.kiwi.com/v2"
search_by_query_endpoint = f"{servers}/search"

now = dt.now() + td(3)
one_year = now + td(days=360)

headers = {
    "apikey": "bHLhdoreTsK2ihiA_jCAkFLVMPpBfNzh",
    "accept": "application/json",
}

params = {
            'date_from': now.strftime("%d/%m/%Y"), # Required (dd/mm/yyyy)
            'date_to': one_year.strftime("%d/%m/%Y"), # Required (dd/mm/yyyy)
            'nights_in_dst_from': 4,
            'nights_in_dst_to': 8,
            'ret_from_diff_city': False, # true is default
            'one_for_city': None, # Returns cheapest flight for every city in fly_to
            'one_per_date': None,
            'adults': 1, # Default 1
            'children': 0, # Default 0
            'infants': 0, # Default 0
            'selected_cabins': None, # M-economy, W-conomy premium, C-business, F-First Class
            'curr': 'USD',}

for destination in top_destinations:
    for origin, option in destination.items():
        for destination, hours in option:
            params['fly_from'] = origin
            params['fly_to'] = destination
            params['max_fly_duration'] = hours # max duration in hours

            pprint(params)
            try:
                response = requests.get(search_by_query_endpoint, headers=headers, params=params).json()

            except:
                print(f"is not available with this criteria\n\n")
                
            else:
                cheapest_data = response['data'][0]
                pprint(cheapest_data)