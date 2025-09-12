import os
import datetime as dt
from amadeus import Client, ResponseError

amadeus = Client(
    client_id = os.getenv("amadeus_key"),
    client_secret = os.getenv("amadeus_secret")
)

# try:
#     response = amadeus.shopping.flight_offers_search.get(originLocationCode="BLR", destinationLocationCode="HND", departureDate="2025-11-19", adults=1, currencyCode="INR")
#     print(response.data)
# except ResponseError as error:
#     print(error)


class FlightSearch:
    def __init__(self, destination, adults, departureDate=dt.datetime.now().strftime("%Y-%m-%d"), origin="BLR"):
        self.destination = destination
        self.departureDate = departureDate
        self.adults = adults
        self.origin = origin
        self.results = []

    def search_flights(self):
        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=self.origin,
                destinationLocationCode=self.destination,
                departureDate=self.departureDate,
                adults=self.adults,
                currencyCode="INR"
            )
            self.results = response.data
            return self.results
        except ResponseError as error:
            print(f"API Error: {error}")
            return []
        
    def change_date(self, days):
        self.departureDate = dt.datetime.now() + dt.timedelta(days=days)