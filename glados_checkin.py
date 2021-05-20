# usr/bin/python
# -*- coding: utf-8 -*-
import requests, json, os
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
SERVER = "on"
# 填写server酱sckey,不开启server酱则不用填
SCKEY = "SCU131982T134cf902075ed7f5179e8b91d7ea75ed5fc7330976360"
# 'SCU89402Tf98b7f01ca3394*********************************'
# 填入glados账号对应cookie
COOKIE = [
	"__cfduid=d9acfaf9bd15e258884514e35c70a7db61609168676; _ga=GA1.2.416012735.1609168680; _gid=GA1.2.1723433426.1609168680; koa:sess=eyJ1c2VySWQiOjYzOTU0LCJfZXhwaXJlIjoxNjM1MDg4NzIyMjQ2LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=um87UXpvKPj3Pf6s-f_IpSvT_ZM",
	"_ga=GA1.2.180625509.1621499157; _gid=GA1.2.508470988.1621499157; koa:sess=eyJ1c2VySWQiOjY3MzU1LCJfZXhwaXJlIjoxNjQ3NDE5NTAyOTM3LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=dWUuouOfq9-SWvz6EQbTZK0npNQ"
]

LOG_FILE = open('log.txt', 'a+', encoding='utf-8')

def check_in():
    url_checkin = 'https://glados.rocks/api/user/checkin'
    payload = {
        'token': "glados_network"
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': '',
        'origin': 'https://glados.rocks',
        'referer': 'https://glados.rocks/console/checkin'
    }

    for cookie in COOKIE:
        headers['cookie'] = cookie
        # print("{}\n".format(headers['cookie']))
        try:
            checkin_response = requests.post(url=url_checkin, headers=headers, data=json.dumps(payload))
            # print("{}\n".format(checkin_response.text))
            checkin_dict = json.loads(checkin_response.text)
            if checkin_dict["code"] == 0:
                print("user_id:{}签到成功！".format(checkin_dict["list"][0]["user_id"]))
                # change_days = str(checkin_dict["list"][0]["change"]).split('.')[0]
                left_days = str(checkin_dict["list"][0]["balance"]).split('.')[0]
                msg = 'user_id: {}, {}, {}天后到期。'.format(checkin_dict["list"][0]["user_id"], checkin_dict["message"], left_days)
            else:
                # change_days = str(checkin_dict["list"][0]["change"]).split('.')[0]
                left_days = str(checkin_dict["list"][0]["balance"]).split('.')[0]
                msg = 'user_id: {}, {}, {}天后到期。'.format(checkin_dict["list"][0]["user_id"], checkin_dict["message"], left_days)
        except Exception as e:
            msg = 'Cookie 失效？{0}'.format(str(e))
            print(str(e))
        finally:
            print(msg)
        if SERVER == 'on':
            requests.get('https://sc.ftqq.com/{0}.send?text={1}'.format(SCKEY, msg))
        LOG_FILE.write('{}\t{}\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg))

if __name__ == '__main__':
	check_in()
