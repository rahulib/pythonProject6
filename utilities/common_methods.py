import requests

# get request
def get_request(url):
    request=requests.get(url)
    return request

