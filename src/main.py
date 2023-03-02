from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import argparse
import requests
import traceback

import transition
import lesson
import data

def main(aDriver):

    tUrl = "https://atr.meijo-u.net"
    if requests.get(tUrl).status_code != 200:
        print(tUrl + "にアクセスできませんでした。")
        return
    aDriver.get(tUrl)
    try:
        transition.Login(aDriver)
    except:
        traceback.print_exc()
        print("IDやPASSWORDか異なっている可能性があります。\n.envを確認し間違っている場合は.envを書き換え\ndocker-compose up -d --build\nを実行してください")
        return
    print("ログイン成功")
    try:
        tResult,tPart = transition.ClassCoursePart(aDriver)
    except:
        traceback.print_exc()
        return
    print(f"{tResult}に移動")
    try:
        tBaseDataPath = data.GetBaseDataPath(tResult,tPart)
    except:
        traceback.print_exc()
        return
    try:
        tWait = WebDriverWait(driver=tDriver, timeout=30)
        lesson.DoLesson(aDriver,tWait)
    except:
        traceback.print_exc()
        return

if __name__ == "__main__":
    try:
        print("START")
        tDriver = webdriver.Remote(
            command_executor = os.environ["SELENIUM_URL"],
            options = webdriver.ChromeOptions()
        )
        main(tDriver)
    finally:
        tDriver.quit()
        print("FINISH")
