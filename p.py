import requests
import json




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "device": "pc"
}



url = 'https://s.alicdn.com/@xconfig/micro_frontend/icbu-im__icbu-alitalk__cl230ll533iy1'
response = requests.get(url)









r = requests.get(url, headers=headers)
data = r.json()
print(data)


with open('lalafo_data2.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    print(f'Данные сохранены в lalafo_data.json')
    
    
    