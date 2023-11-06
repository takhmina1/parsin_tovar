import requests
import json




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "device": "pc"
}



# url = 'https://lalafo.kg/api/search/v3/feed/details/72500423?expand=url'

# url = 'https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gpt&tv=m202310240101&st=env'

url = 'https://s.alicdn.com/@xconfig/micro_frontend/icbu-im__icbu-alitalk__cl230ll533iy1'

response = requests.get(url)
# Отправьте GET-запрос к API









r = requests.get(url, headers=headers)
data = r.json()
print(data)


# with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
#     json.dump(data, file, indent=2, ensure_ascii=False)
#     print(f'Данные сохранены в lalafo_data.json')
    
    

with open('lalafo_data4.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    print(f'Данные сохранены в lalafo_data.json6')
    
    