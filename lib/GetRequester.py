import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        try:
            json_data = json.loads(response_body)
            return json_data
        except ValueError:
            print("Error: Response body is not valid JSON.")
            return None
