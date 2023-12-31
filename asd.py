import requests
import json
import xmltodict
from urllib.parse import quote


base_url = "#"
endpoint = "#"
service_key = "#"

item_name = '케토라신정a'
encoded_item_name = quote(item_name)
url = f"{base_url}{endpoint}?serviceKey={service_key}&itemName={encoded_item_name}"

response = requests.get(url)
response_dict = xmltodict.parse(response.text)
items = response_dict['response']['body']['items']['item']


for item in items:

    print(f"TYPE_NAME: {item['TYPE_NAME']}")
    print(f"ITEM_NAME: {item['ITEM_NAME']}")
    print(f"MIXTURE_INGR_KOR_NAME: {item['MIXTURE_INGR_KOR_NAME']}")
    print(f"INGR_ENG_NAME: {item['INGR_ENG_NAME']}")
    print(f"MIXTURE_ITEM_NAME: {item['MIXTURE_ITEM_NAME']}")
    print("INGR_CODE: ", item['INGR_CODE'])
    print("PROHBT_CONTENT: ", item['PROHBT_CONTENT'])
    print("ENTP_NAME: ", item['ENTP_NAME'])
    print("\n")