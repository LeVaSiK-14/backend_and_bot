import requests


class SendRequest:
    def __init__(self, method=''):
        self.method = method

    def send_url(self, url, headers=None, data=''):
        if self.method == 'POST':
            response = requests.post(
                url=url, data=data, headers=headers)
            return response.json()
        elif self.method == 'GET':
            response = requests.get(url=url, headers=headers)
            return response.json()
        else:
            raise ValueError({"Error": f"Method {self.method} incorrect!"})
