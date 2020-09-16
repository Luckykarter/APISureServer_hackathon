import requests


def test_connection(url):
    res = requests.post(url)
    results = res.json().get('results')

# def get_access_token():
