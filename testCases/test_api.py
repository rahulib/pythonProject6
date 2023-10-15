import requests
from utilities.config import url
from utilities.common_methods import get_request

def test_git():
    r=get_request(url)
    assert r.status_code==200
    print(r.json())
    for j in r.json():
        e=j['type'][1]
        print(e)
        assert e==e

test_git()