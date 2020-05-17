# 1.	Посмотреть документацию к API GitHub,
# разобраться как вывести список депозитариев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json

import requests
import json5
import get
main_link = 'https://api.github.com'
name_user = input('Введите имя пользователя GitHub')
url = '/users/' + name_user + '/repos'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                        'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'}
response = requests.get(main_link + url, headers = header)
if response.ok:
    list_repos = repos = json5.loads(response.text)
    n = 1
    for i in list_repos:
        print(str(n) + ' ' + i['name'])
        n+= 1
        with open(name_user + '.json5', "w", encoding = "utf-8") as f:
            f.write(response.text)