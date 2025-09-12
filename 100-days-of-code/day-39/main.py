import flight_search as fs

haneda = fs.FlightSearch(destination="HND", adults=1)
haneda.search_flights()
print(haneda.results)