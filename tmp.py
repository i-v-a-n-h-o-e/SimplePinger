import datetime
import random
import time

import requests
import os

url = 'yandex.ru'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
url2request = 'https://' + url

while True:
    with open('log.txt', 'a') as log:
        now = datetime.datetime.now()
        ping_status = os.system('ping -c 1 %s' % (url,))

        if ping_status == 0:
            try:
                r = requests.get(url2request, headers=headers)
                req_status = str(r.status_code)
            except requests.exceptions.RequestException:
                req_status  = "Time error"
        else:
            r = "ping error"

        status = str(now) + '\t' + str(r) + '\n'
        log.writelines(status)
        print(status)
    time.sleep(random.randrange(55, 65))