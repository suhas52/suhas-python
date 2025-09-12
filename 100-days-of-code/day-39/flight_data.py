class FlightData:
    #This class is responsible for structuring the flight data.
    pass

import datetime

for i in range(40):
    date = datetime.datetime.now() + datetime.timedelta(days=i)
    print(date)
