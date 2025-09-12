import os
import datetime
from amadeus import Client, ResponseError

amadeus = Client(
    client_id = os.getenv("amadeus_key"),
    client_secret = os.getenv("amadeus_secret")
)

try:
    response = amadeus.shopping.flight_offers_search.get(originLocationCode="BLR", destinationLocationCode="HND", departureDate="2025-11-19", adults=1, currencyCode="INR")
    print(response.data)
except ResponseError as error:
    print(error)


# # class FlightSearch:
# #     def __init__():
        