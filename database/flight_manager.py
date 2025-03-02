from datetime import datetime as dt, timedelta as td
from pprint import pprint
import requests
import sqlite3

top_destinations = [
    {"GUA": [("LAX", 10), ("NYC", 10), ("MEX", 10), ("SJO", 10), ("MAD", 20), ("FRS", 10), ("CUN", 10), ("MIA", 10), ("BOG", 10), ("WAS", 10), ("HOU", 10), ("FLL", 10), ("CTG", 10), ("BOS", 10), ("LIM", 10), ("SDQ", 10), ("ORL", 10), ("PTY", 10), ("CHI", 10), ("SFO", 10), ("MGA", 10), ("MDE", 10), ("ATL", 10), ("PUJ", 10), ("SAL", 10), ("DFW", 10), ("LAS", 10), ("SJU", 10), ("SXM", 10), ("AMS", 20), ("SCL", 20), ("BCN", 20), ("FRA", 20), ("RTB", 10), ("BZE", 10), ("YMQ", 10), ("SAP", 10), ("LON", 20), ("GDL", 10), ("CUR", 10), ("DEN", 10), ("YVR", 10), ("YTO", 10), ("SEA", 10), ("PAR", 20), ("AUA", 10), ("MUC", 20), ("BUE", 20), ("PHL", 10), ("SLC", 10), ("UIO", 10), ("BER", 20), ("BRU", 20), ("RDU", 10), ("BNA", 10), ("ASU", 10), ("CLT", 10), ("CUZ", 10), ("TPA", 10), ("PHX", 10), ("MTY", 10), ("PDX", 10), ("MSY", 10), ("SEL", 30), ("TYO", 20), ("VIE", 20), ("TLV", 20), ("LIS", 20), ("XPL", 10), ("MED", 30), ("AUS", 10), ("MVD", 20), ("MSP", 10), ("CPH", 20), ("IST", 20), ("BKK", 30), ("OAX", 10), ("SAO", 20), ("HAM", 20), ("IND", 10), ("SJD", 10), ("SAT", 10), ("ROM", 20), ("RIO", 20), ("GYE", 10), ("CLO", 10), ("OMA", 10), ("YYC", 10), ("CCS", 10), ("TIJ", 10), ("DUS", 20), ("WAW", 20), ("SJC", 10), ("CMH", 10), ("CLE", 10), ("CAI", 30), ("DUB", 20), ("DTT", 10), ("TGU", 10)]},
    # {"GUA": [("LAX", 10), ("NYC", 10), ("MEX", 10)]}
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

data = []

for destination in top_destinations:
    for origin, option in destination.items():
        for destination, hours in option:
            params['fly_from'] = origin
            params['fly_to'] = destination
            params['max_fly_duration'] = hours # max duration in hours

            pprint(f"Getting data for {params['fly_to']}")
        
            response = requests.get(search_by_query_endpoint, headers=headers, params=params).json()

            try:
                cheapest_data = response['data'][0]
            
            except IndexError:
                print(f"{params['fly_to']} not available with this criteria")

            else:
                time_now = str(dt.now())
                deep_link = response['data'][0]['deep_link']
                city_to = response['data'][0]['cityTo']
                price = response['data'][0]['price']
                nightsInDest = response['data'][0]['nightsInDest']
                cityFrom = response['data'][0]['cityFrom']
                cityTo = response['data'][0]['cityTo']
                flight_info = (time_now, origin, destination, cityFrom, cityTo, deep_link, price, nightsInDest)
                data.append(flight_info)


# con = sqlite3.connect("./database/flying_chip.db")
con = sqlite3.connect('/home/reyner/flying_chip/database/flying_chip.db')
cur = con.cursor()


cur.executemany("""
INSERT INTO cheapest_flights (time_now, cityCodeFrom, cityCodeTo, cityFrom, cityTo, deep_link, price, nightsInDest) VALUES
            (?,?,?,?,?,?,?,?)""", data)

con.commit()
