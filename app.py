import time
import sys
import os

# logo
import base64
from io import BytesIO
from PIL import Image, ImageQt

## For Selenium WebBot
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import tkinter as tk

## For Line ##
import requests

from PyQt6.QtWidgets import QApplication, QWidget, QDateEdit, QPushButton, QFormLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from datetime import datetime, timedelta

logo = b'iVBORw0KGgoAAAANSUhEUgAAAUAAAAA3CAMAAABKHmNVAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAPlQTFRFAAAAAP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//GP/nXv+hMP/PYP+f//8A1v8pvv9BeP+HSP+3dv+J7v8RkP9v8P8PqP9Xjv9xwP8/pv9Z2P8nAP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//AP//Z2s1+QAAAFN0Uk5TADuPzfL/1r6xjE7uIF6DkC+05aibdjhzHlyBvH4qRbcsgM9dHUO1dDZPB9ijwv///////////////////////6Wq2h/AdefwN7OOUGimywiN4xRKwGXzAAAH00lEQVR4nO1baXubRhBWYlPlsOI4ttMkbaTEbdMmaRHIgAUYk0N26lxt8/9/TGHZY2Z2FiHLR/1U7xfBnjMvM7OzK+j1VljhQnDj5tq6912/f+v2nbP0VFhfu3lD19y5fasP0WVs0aca6C5pvjG4t+nNxfoanlFg8x4pWFxHJdldW8kG97eAFA88b3tn92G3YVHPBlv3Rc33DxgNmTIjzqPHT0j9gx9+fFrXDEfzyVsInGxuwXrPnvdJj0rJmtHNe4ONqn7A9d/7qQN/bE9v0Ov93F9En0qcp7+84Ot+/a3XwfYuCNJmuSrN6Gj40tF7+5WDNuS1PF4vKOnvLXVrC47138EfLIOM167gwHZnr12Bhx0HV/wthD3Lf69aousGms2s4t+C2CUEso38sURwydJdAXy3kuFkP4ooCTtdCAwnCqQiiCBiLxnb8EmXgyiqBppWopDB0slcJJ4XWUhDUhB3JQsjGUdTTkmNzAiS60K6DrM9nQSGWD+PUzoE7f1DVDU9gIMV8wmsxmJKacfCEoyFk55U3AfVw49SKDzoa6xwOQskciYOpZUEU7v26MoIzGr5gd0ywk0mJVA2Z4ufPH7EEzhfgtKSs+SaaQIdSiVXRGDRZcoCEAiK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'


branch = "大阪"

report_list = {'data':[]}

yahoousername = "vdsku24176"
yahoopasscode = "Masa!0928"

kaitoriusername = "op_sawamura"
kaitorimycode = "gracesawamura"

findsalelist = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def loginyahoo(driver, username, passcode):
    time.sleep(1)
    driver.find_element(By.ID, "login_handle").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "#content > div.loginAreaBox > div > form > div:nth-child(1) > div.stack > div:nth-child(2) > div > button").click()
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(passcode)
    driver.find_element(By.CSS_SELECTOR, "#content > div.loginAreaBox > div > form > div:nth-child(2) > div > div:nth-child(1) > div.stack > div.login.ar-button_button_J2jv2.ar-button_medium_1i9SB.ar-button_normal_1m_gx.ar-button_fullwidth_19rcY > button").click()

def gotoyahoosalelist(driver):
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"ycWrStrTopLeft\"]/div[3]/h2")))
    findsalelist = True
    time.sleep(1)
    driver.get("https://auctions.store.yahoo.co.jp/serinavi/sold-list")
    time.sleep(10)

def addtokaitori(soleday):
    yesterday = datetime(int(soleday.split('-')[0]), int(soleday.split('-')[1]), int(soleday.split('-')[2])) - timedelta(days=1)

    print(yesterday.day)
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://login.yahoo.co.jp/config/login?.src=bizmgr&.lg=jp&.intl=jp&.suppreg_skip=1&.done=https%3A%2F%2Flogin.bizmanager.yahoo.co.jp%2Fyidlogin%3F.pass%3D0%26.done%3Dhttps%253A%252F%252Fpro.store.yahoo.co.jp%252Fpro.kaitoriyasan1%26.src%3Dnone")
        WebDriverWait(driver,600).until(EC.visibility_of_element_located((By.ID, "login_handle")))
        loginyahoo(driver, yahoousername,yahoopasscode)
        while (findsalelist == False):
            try:
                gotoyahoosalelist(driver)
                break
            except TimeoutError as ex:
                WebDriverWait(driver,600).until(EC.visibility_of_element_located((By.ID, "login_handle")))
                loginyahoo(driver, yahoousername,yahoopasscode)

        i = 2
        page = 1

        while (True):
            if (i<=101):
                year = driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[1]/div/main/div/div/div[5]/div/div/ul[" + str(i) + "]/li[9]/div/div/p[1]").text
                month = driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[1]/div/main/div/div/div[5]/div/div/ul[" + str(i) + "]/li[9]/div/div/p[2]").text.split('/')[0]
                days = driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[1]/div/main/div/div/div[5]/div/div/ul[" + str(i) + "]/li[9]/div/div/p[2]").text.split('/')[1]
                soldDate = year + '-' + month + '-' + days

                if (soleday == soldDate):
                    sku = driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[1]/div/main/div/div/div[5]/div/div/ul[" + str(i) +"]/ li   [3]/div/div/p[3]").text
                    price = driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[1]/div/main/div/div/div[5]/div/div/ul[" + str(i)+   "]/li [4]/div").text.replace('円','').replace(',','')
                    report_list["data"].append({'sku':sku.replace('管理番号 ',''), 'price':price, 'date':soldDate})
                    # print("Product " + str(i - 1))
                    # print("SKU : " + sku.replace('管理番号 ',''))
                    # print("Price : " + price)
                    # print("Date : " + soldDate)
                    i += 1

                elif (yesterday.year == int(year) and yesterday.month == int(month) and yesterday.day == int(days)):
                    break
                    
                else:
                    i += 1

            else:
                page += 1
                driver.get("https://auctions.store.yahoo.co.jp/serinavi/sold-list?page=" + str(page))
                time.sleep(10)
                i = 2

        print(report_list)

        # Parameter
        ## parameter-login

        print("[UPDATE] Gracekaitori System")

        ## Login 
        driver.get("https://gracekaitori.com/index.php")
        driver.find_element(By.NAME, "uid").send_keys(kaitoriusername)
        driver.find_element(By.NAME, "pwd").send_keys(kaitorimycode)
        driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
        print("[Login] Gracekaitori Successfully")
        time.sleep(1)

        line_message =  "\nヤフオク関西買取" + '\n' + \
                        '\n' + \
                        '点数 ' + '{:,}'.format(len(report_list["data"])) + '点' + '\n' + \
                        '\n'

        for product in report_list["data"]:
            driver.get("https://gracekaitori.com/stocklist.php")
            time.sleep(1)
            driver.find_element(By.NAME, "q").send_keys(product['sku'])
            driver.find_element(By.CSS_SELECTOR, "i[class=\"icon-search\" i]").click()

            ## Check exist data
            try:
                check_cost_exist = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/table/tbody/tr[8]/td[7]").text
                if check_cost_exist == branch:

                    ## Edit status
                    time.sleep(1)
                    driver.find_element(By.CSS_SELECTOR, "img[src=\"./images/btnedit.jpg\" i]").click()

                    ## Fill form
                    time.sleep(1)
                    driver.find_element(By.NAME, "itemprice").clear()
                    driver.find_element(By.NAME, "itemprice").send_keys(str(round(int(product['price']) / 1.1)))
                    print(driver.find_element(By.XPATH, "//*[@id=\"sold\"]").get_attribute('checked'))
                    if (driver.find_element(By.XPATH, "//*[@id=\"sold\"]").get_attribute('checked') == None):
                        driver.find_element(By.XPATH, "//*[@id=\"sold\"]").click()

                    driver.find_element(By.NAME, "solddate").clear()
                    driver.find_element(By.NAME, "solddate").send_keys(product['date'])

                    ## Submit update
                    driver.find_element(By.XPATH, "//*[@id=\"form1\"]/table/tbody/tr[29]/td").click()

                    ## Confirm 
                    time.sleep(1)
                    driver.find_element(By.XPATH, "//*[@id=\"modal\"]/button[2]").click()

                    print(product['sku'] + ' Success')

                    line_message += product['sku'] + '\n' + \
                                    "売却 : " + '{:,}'.format(round(int(product['price']))) + ' 円\n' + \
                                    '実際 : ' + '{:,}'.format(round(int(product['price']) / 1.1)) + ' 円\n' + \
                                    '\n'
            except Exception as e:
                url_line = 'https://notify-api.line.me/api/notify'
                token = 'xMeOA5w8PPaGrIUXrCqAfh7BBg2jz4sd1czAmqdkgx5'
                headers = {'content-tpye': 'application/x-www-form-urlencoded',
                           'Authorization': 'Bearer '+token}
                msg = "\n\nFrom : {}\n\n Error : {}\n\n SKU : {}".format(branch,e,product['sku'])
                resp_line = requests.post(
                url_line, headers=headers, data={'message': msg})

        driver.close()

        sendlinenoti(line_message)

        return "終了した。"
    
    except Exception as e:
        url_line = 'https://notify-api.line.me/api/notify'
        token = 'xMeOA5w8PPaGrIUXrCqAfh7BBg2jz4sd1czAmqdkgx5'
        headers = {'content-tpye': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer '+token}
        msg = "\n\nFrom : {}\n\n Error : {}".format(branch,e)
        resp_line = requests.post(
        url_line, headers=headers, data={'message': msg})

        return "エラーがあります。 エンジニアに連絡してください。"

    

def sendlinenoti(line_message):
    url_line = 'https://notify-api.line.me/api/notify'
    token = 'PLwp35l0np3WXLgGcuqu7Vdr4eFDTbUj8IcOJ0cZyd5'
    headers = {'content-tpye': 'application/x-www-form-urlencoded',
               'Authorization': 'Bearer '+token}
    msg = line_message
    resp_line = requests.post(
    url_line, headers=headers, data={'message': msg})


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        byte_data = base64.b64decode(logo)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)

        qImage = ImageQt.ImageQt(image)

        yesterday = datetime.now() - timedelta(days = 1)

        self.setWindowTitle('大阪ヤフオク買取')
        self.setMinimumWidth(200)

        # create a grid layout
        layout = QFormLayout()
        self.setLayout(layout)

        self.label = QLabel(self)
        self.logo = QPixmap.fromImage(qImage)
        self.label.setPixmap(self.logo)

        self.date_edit = QDateEdit(self)
        self.date_edit.setDate(yesterday)

        self.button = QPushButton("OK")
        self.button.clicked.connect(self.submit)

        self.result_label = QLabel('', self)

        layout.addRow(self.label)
        layout.addRow('販売日 :', self.date_edit)
        layout.addRow(self.button)
        layout.addRow(self.result_label)

        self.show()

    def submit(self):
        self.result_label.setText("今しばらくお待ちください。。。")
        value = self.date_edit.date()
        soleday = u'{:04d}-{:02d}-{:02d}'.format(value.year(), value.month(), value.day())
        # print(soleday)
        
        status = addtokaitori(soleday)
        
        self.result_label.setText(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())