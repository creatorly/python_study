#!/usr/bin/python

import requests
import functools
import time
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import json
import random


class CheckInfo(object):
    def __init__(self, result, count, start_time, use_time):
        self.result = result  # 判断模块是否检测完成，0-未完成，1-完成
        self.count = count    # 测试次数
        self.start_time = start_time  # 测试起始时间
        self.use_time = use_time  # 测试用时

    time_out = 0
    browser = 0


class LinkInfo(object):
    def __init__(self, url):
        self.url = url    # 地址

    http_head = ""   # http头部
    http_body = ""   # http值
    enter_msg = ""   # 输入信息
    return_msg = ""  # 返回信息


check = CheckInfo(0, 0, time.time(), 0)
check.time_out = 0
tlink = LinkInfo("https://tlinkapi.ziroom.com/doc/index")


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
    if False == os.path.exists("log"):
        print("log file don't exist.create")
        os.mkdir("log")
    else:
        print("log file exist")

    logging.basicConfig(  # filename="log/test.log", # 指定输出的文件
        level=logging.DEBUG,
        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    logging.info("#######################test start#######################")


def browser_init():
    # 绑定浏览器
    CheckInfo.browser = webdriver.Chrome()
    # 最大化浏览器
    CheckInfo.browser.maximize_window()
    # 打开页面
    url = tlink.url
    CheckInfo.browser.get(url)

    # 点击zHelp
    CheckInfo.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[4]/div/div[2]/div/div/div/div[3]/table/tbody/tr/td[1]').click()
    # 点击设备控制
    CheckInfo.browser.find_element_by_xpath('//*[@id="gwt-uid-8"]/div/div').click()
    # 点击测试
    CheckInfo.browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[4]/div/div[4]/div/div/div/table[1]/tbody/tr/td[2]/button').click()
    # 点击http头
    CheckInfo.browser.find_element_by_xpath('/html/body/div[5]/div/table/tbody/tr[2]/td[2]/div/div/div[2]/table/tbody/tr/td[2]/table/tbody/tr/td[4]/button').click()
    # 输入http头
    tlink.http_head = "GATEWAY-VALIDATE"
    CheckInfo.browser.find_element_by_xpath('/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table[1]/tbody/tr/td[2]/input').clear()
    CheckInfo.browser.find_element_by_xpath('/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table[1]/tbody/tr/td[2]/input').send_keys(tlink.http_head)
    # 输入http值
    tlink.http_body = "kLSIUlsSLILEKXasAAALIELKFJCKSILidksKALSIDKCKAKSIDKOA"
    CheckInfo.browser.find_element_by_xpath('/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table[2]/tbody/tr/td[2]/input').clear()
    CheckInfo.browser.find_element_by_xpath('/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table[2]/tbody/tr/td[2]/input').send_keys(tlink.http_body)
    # 点击添加
    CheckInfo.browser.find_element_by_xpath('/html/body/div[6]/div/table/tbody/tr[2]/td[2]/div/div/table[3]/tbody/tr/td[1]/button').click()
    logging.info("browser_init ok")


@try_fun
def start_addpasswd_test():

    CheckInfo.browser.find_element_by_xpath('//*[@id="_aceGWT0"]/div[2]/div').clear()
    CheckInfo.browser.find_element_by_xpath('//*[@id="_aceGWT0"]/div[2]/div').send_keys("test")

    '''
    url = 'https://tlinkapi.ziroom.com/v1/zhelp/device/control'
    payload = {
        "msgType": "DEVICE_CONTROL",
        "devId": "F206E34470A0C440",
        "prodTypeId": "YG0002",
        "time": "2018-05-14 10:10:10",
        "sno": "789",
        "command": "add_password",
        "attribute": "lock_password",
        "data": [{
            "k": "index",
            "v": "0"
        }, {
            "k": "content",
            "v": "12345678"
        }]
    }
    headers = {'GATEWAY-VALIDATE': 'kLSIUlsSLILEKXasAAALIELKFJCKSILidksKALSIDKCKAKSIDKOA',
               'content-type': 'application/json'}

    if check.count < 100:
        payload["data"][0]["v"] = check.count
        payload["data"][1]["v"] = random.randint(000000, 9999999)
        logging.info(payload)
        result = requests.post(url, data=json.dumps(payload), headers=headers)
        logging.info(result.text)
        if result.status_code == 200:
            msg = json.loads(result.text)
            if 200 == msg["code"]:
                check.count += 1
            else:
                logging.info("test finish")
                check.result = 1
        else:
            logging.info(result)
            check.result = 1
    else:
        logging.info("test finish")
        check.result = 1
    '''


def stop_test():
    exit()


if __name__ == '__main__':
    logging_init()
    browser_init()
    while True:

        if 0 == check.result:
            start_addpasswd_test()
        else:
            stop_test()

        time.sleep(3)
