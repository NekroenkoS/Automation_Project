import operator
from functools import reduce

import requests

header = {'x-api-key': 'reqres-free-v1', 'Content-Type': 'application/json'}

# Common API interaction helpers for readability and consistency
class APIActions:

    @staticmethod
    def get(path, params=None):
        response = requests.get(path, headers=header, params=params)
        return response

    @staticmethod
    def extract_value_from_response(response, nodes):
        response_json = response.json()
        return reduce(operator.getitem, nodes, response_json)

    @staticmethod
    def post(path, payload):
        response = requests.post(path, headers=header, json=payload)
        return response

    @staticmethod
    def put(path, payload):
        response = requests.put(path, headers=header, json=payload)
        return response

    @staticmethod
    def delete(path):
        response = requests.delete(path, headers=header)
        return response
