import requests


class APISureConnector:
    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_url = 'https://api.apisure.io/oauth/client_credential/accesstoken?grant_type=client_credentials'
        self.token = self.get_token()

    def get_token(self):
        data = {
            'client_id': self._client_id,
            'client_secret': self._client_secret
        }
        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '73',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'api.apisure.io',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(self._token_url, data=data, headers=headers)
        response = response.json()
        return response.get("access_token")

    def send_request(self, url, data=None):
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'X-Apisure-Sender-ID': 'ImexConsumerBASE',
            'X-Apisure-Reciepent-ID': 'IMEXBase8',
        }

        response = requests.post(url, json=data, headers=headers)
        return response
