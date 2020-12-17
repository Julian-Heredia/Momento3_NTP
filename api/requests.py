import requests

class RequestApi:
    url = 'https://api.punkapi.com/v2/beers/'

    @staticmethod
    def get_oneBeer(id):
        try:
            response = requests.request("GET", RequestApi.url+"/"+id)
            if response.status_code != 200:
                return False
            else:
                return response.json()
        except:
            return False