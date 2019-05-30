#!/usr/bin/python

import requests
import functools
import time
import os
import logging
import json
import unittest
import uuid


def try_fun(func):
    if callable(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            try:  # 进行异常捕获
                response = func(*args, **kw)
            except Exception as e:
                print(e)
                response = None
            return response
        return wrapper
    else:
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                try:  # 进行异常捕获
                    response = fn(*args, **kw)
                except Exception as e:
                    print(e)
                    response = None
                return response
            return wrapper
        return decorator


def logging_init():
    if 0 == os.path.exists("log"):
        print("log file don't exist.create")
        os.mkdir("log")
    else:
        print("log file exist")

    logging.basicConfig(  # filename="log/test.log", # 指定输出的文件
        level=logging.DEBUG,
        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    return True


@try_fun
def start_repeat_setpower(max_count):
    url = 'https://tlink.zihome.com/link-handle-gateway/v1/operate/device/control'
    payload = {
        "msgType": "DEVICE_CONTROL",
        "devId": "01100115af",
        "prodTypeId":   "8grteg3l",
        "time": "2018-05-14 10:10:10",
        "sno": "789",
        "attribute": "light_power",
        "command": "set_power",
        "data": [{
            "k": "power",
            "v": "0"
        }]
    }
    headers = {'GATEWAY-VALIDATE': 'kLSIUlsSLILEKXasAAALIELKFJCKSILidksKALSIDKCKAKSIDKOA',
               'content-type': 'application/json'}

    i = 0
    power_value = 0

    while i < max_count:
        if 0 == power_value:
            power_value = 1
            payload["sno"] = str(uuid.uuid1())
            payload["data"][0]["v"] = "1"
        else:
            power_value = 0
            payload["sno"] = str(uuid.uuid1())
            payload["data"][0]["v"] = "0"

        logging.info(payload)
        result = requests.post(url, data=json.dumps(payload), headers=headers, timeout=(5, 5))
        logging.info(result.text)
        if result.status_code == 200:
            msg = json.loads(result.text)
            if 200 == msg["code"]:
                i += 1
            else:
                return False
        else:
            return False

        time.sleep(3)

    return True


def start_repeat_setbright(max_bright):
    url = 'https://tlink.zihome.com/link-handle-gateway/v1/operate/device/control'
    payload = {
        "msgType": "DEVICE_CONTROL",
        "devId": "01100115af",
        "prodTypeId":   "8grteg3l",
        "time": "2018-05-14 10:10:10",
        "sno": "789",
        "attribute": "light_bright",
        "command": "set_bright",
        "data": [{
            "k": "bright",
            "v": "0"
        }]
    }
    headers = {'GATEWAY-VALIDATE': 'kLSIUlsSLILEKXasAAALIELKFJCKSILidksKALSIDKCKAKSIDKOA',
               'content-type': 'application/json'}

    bright_value = 1

    while bright_value < max_bright:
        payload["sno"] = str(uuid.uuid1())
        payload["data"][0]["v"] = str(bright_value)

        logging.info(payload)
        result = requests.post(url, data=json.dumps(payload), headers=headers, timeout=(5, 5))
        logging.info(result.text)
        if result.status_code == 200:
            msg = json.loads(result.text)
            if 200 == msg["code"]:
                bright_value += 10
            else:
                return False
        else:
            return False

        time.sleep(3)

    return True


def start_repeat_settemperature(max_temperature):
    url = 'https://tlink.zihome.com/link-handle-gateway/v1/operate/device/control'
    payload = {
        "msgType": "DEVICE_CONTROL",
        "devId": "01100115af",
        "prodTypeId":   "8grteg3l",
        "time": "2018-05-14 10:10:10",
        "sno": "789",
        "attribute": "light_temperature",
        "command": "set_temperature",
        "data": [{
            "k": "temperature",
            "v": "0"
        }]
    }
    headers = {'GATEWAY-VALIDATE': 'kLSIUlsSLILEKXasAAALIELKFJCKSILidksKALSIDKCKAKSIDKOA',
               'content-type': 'application/json'}

    temperature_value = 0

    while temperature_value < max_temperature:
        payload["sno"] = str(uuid.uuid1())
        payload["data"][0]["v"] = str(temperature_value)

        logging.info(payload)
        result = requests.post(url, data=json.dumps(payload), headers=headers, timeout=(5, 5))
        logging.info(result.text)
        if result.status_code == 200:
            msg = json.loads(result.text)
            if 200 == msg["code"]:
                temperature_value += 10
            else:
                return False
        else:
            return False

        time.sleep(3)

    return True


class TestLedMethods(unittest.TestCase):

    def setUp(self):
        print("init by setUp...")

    def tearDown(self):
        print("end by tearDown...")

    def test_00logging_init(self):
        print("test_00logging_init")
        self.assertTrue(logging_init())

    def test_01repeat_setpower(self):
        print("test_01repeat_setpower")
        self.assertTrue(start_repeat_setpower(5))

    def test_02repeat_setbright(self):
        print("test_02repeat_setbright")
        self.assertTrue(start_repeat_setbright(100))

    def test_03repeat_settemperature(self):
        print("test_03repeat_settemperature")
        self.assertTrue(start_repeat_settemperature(1000))


if __name__ == '__main__':
    unittest.main()
