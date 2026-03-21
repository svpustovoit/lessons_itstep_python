#import urllib.request

#opener = urllib.request.build_opener()
#responce = opener.open("https://httpbin.org/get")
#print(f"responce.read(): {responce.read()}")
'''
import requests

responce = requests.get("https://httpbin.org/get")
print(responce.content)
print(f"datatype responce - {type(responce.content)}")
print(f"responce.text - {responce.text}")

responce_2 = requests.get("https://httpbin.org")
print(responce_2.content)
print(f"datatype responce_2 - {type(responce_2.content)}")
print(f"responce_2.text - {responce_2.text}")


import requests

responce = requests.post("https://httpbin.org/post",
                         data="Test data",
                         headers={"h1": "Test title"})

print(f"responce.text - {responce.text}")

responce_2 = requests.post("https://httpbin.org/post",
                         data={"Test form": "my_form"},
                         )

print(f"responce_2.text - {responce_2.text}")
'''

import requests

responce = requests.get("https://coinmarketcap.com/")

print(f"responce.text - \n\t\t{responce.text}")
print()

responce_text = responce.text
responce_parse = responce_text.split("<span>")
print(f"responce_parse - {responce_parse}")
print()

result_parse_list = []

for parse_elem_1 in responce_parse:
    if parse_elem_1.startswith("$"):
        #print(parse_elem_1)
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                result_parse_list.append(parse_elem_2)
                print(parse_elem_2)

print(f"result_parse_list - {result_parse_list}")

bitcoin_exchange_rate = result_parse_list[1]
print(f"bitcoin_exchange_rate - {bitcoin_exchange_rate}")









