import connexion
import six
import requests
import json
import urllib
from uber_request import get_time_estimate

from urllib.parse import quote, urlencode
from pprint import pprint
from uber_rides.session import Session
from uber_rides.client import UberRidesClient


from swagger_server.models.estimated_time import EstimatedTime  # noqa: E501
from swagger_server import util


def get_time_post(body):  # noqa: E501
    """obtener tiempo estimado con las locaciones

     # noqa: E501

    :param body: hello
    :type body: dict | bytes

    :rtype: None
    """
    session = Session(server_token='Z_ubRQ6CIPlHGedtNc__jbc4nAHkunUYh3iNFH18')

    if connexion.request.is_json:
        body = EstimatedTime.from_dict(connexion.request.get_json())  # noqa: E501
        estimate = get_time_estimate(session,body.latitud_inicial,body.longitud_inicial,body.latitud_final,body.longitud_final)
        #tiempo en segundos

    return estimate #tiempo en minutos
