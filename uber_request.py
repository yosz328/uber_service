import requests

from uber_rides.session import Session
from uber_rides.client import UberRidesClient

def get_time_estimate( session, lat1, lon1, lat2, lon2):


    client = UberRidesClient(session)

    response = client.get_price_estimates(
        start_latitude=lat1,
        start_longitude=lon1,
        end_latitude=lat2,
        end_longitude=lon2,
        seat_count=2
        )

    estimate = response.json.get('prices')
    
    
    data = {
            "Duracion": estimate[7]['duration']/60,
            "alto_estimado": estimate[7]['high_estimate'],
            "bajo_estimado": estimate[7]['low_estimate']
            }





    return data
