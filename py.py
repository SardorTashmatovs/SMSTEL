# 71d410a3b565ad88c5d9ff93de6b70ea41c04e88
# API key in smstel

import requests
API_KEY = '71d410a3b565ad88c5d9ff93de6b70ea41c04e88'
i1 = int(input('Ведите число 1 для отправки сообщения, или число 2 для того чтобы узнать данные своего телефона:'))

match i1:
    case 1:
        phone = "998330331733"
        message = "Helloooooooooooooo"
        device = "2319"
        sim = "1"
        priority = "1"
        params = {'key': API_KEY, 'phone' :phone, 'message': message, 'device': device, 'sim': sim, 'priority': priority}
        url = requests.post('https://smstel.ru/api/send',params=params)
        a = url.json()
        if a['status'] == 200:
            print('успешно')
        else:
            print('неуспешно')
    case 2:
        param = {'id': '2319'}
        sas = requests.get(f'https://smstel.ru/api/get/device?key={API_KEY}', params=param)
        hh = sas.json()
        print(f" версия твоего телефона: {hh['data']['name']}\n Версия твоего телефона: {hh['data']['version']}\n имя версии телефона: {hh['data']['version_name']}\n Марка : {hh['data']['manufacturer']}")
    case _:
        print("вы ввели неправильное число")