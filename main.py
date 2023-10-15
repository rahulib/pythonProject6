# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# import requests
#
# headers = {
#   'Content-Type': 'application/json'
# }
# credentials={"username:""dGFOYQ==" "password:""U2FsdGVkX1974CQPT3eKjNpIPPsojssg7HDC99WkzZU="}
# r=requests.post("https://cms.bheem.tv/v1/login",headers=headers,json=credentials)
# print(r.url)
# print(r.json())
# print(r.status_code())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
url = "https://cmsd.bheem.tv/v1/login"

payload = json.dumps({
  "username": "dGFOYQ==",
  "password": "U2FsdGVkX1974CQPT3eKjNpIPPsojssg7HDC99WkzZU="
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
