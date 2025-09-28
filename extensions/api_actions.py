import requests

header = {'x-api-key': 'reqres-free-v1', 'Content-Type': 'application/json'}


class APIActions:

    @staticmethod
    def get(path, params=None):
        response = requests.get(path, headers=header, params=params)
        return response

    @staticmethod
    def extract_value_from_response(response, nodes):
        extracted_value = None
        response_json = response.json()
        if len(nodes) == 1:
            extracted_value = response_json[nodes[0]]
        elif len(nodes) == 2:
            extracted_value = response_json[(nodes[0])][(nodes[1])]
        elif len(nodes) == 3:
            extracted_value = response_json[(nodes[0])][(nodes[1])][(nodes[2])]
        return extracted_value

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
