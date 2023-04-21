import time
import sys
import os

## For Selenium WebBot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import tkinter as tk

## For Line ##
import requests

## For Datetime
import datetime

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

window = tk.Tk()

window.geometry("400x200")

window['background']='#ffffff'

label = tk.Label(text="How many Product (n >= 1)")
label.pack()

loopnum = tk.Entry()
loopnum.pack()

submit_button = tk.Button(text="Submit")
submit_button.pack()

def submit_input():
    loop = loopnum.get()
    driver = webdriver.Chrome(options=options, executable_path=resource_path('driver/chromedriver'))

    driver.get("https://seller.shopee.co.th/")

    wait = WebDriverWait(driver, 600)
    order_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sidebar-container"]/div/ul/li[2]/ul/li[1]/a')))

    driver.get("https://seller.shopee.co.th/portal/sale/order?type=completed")

    waitsku = WebDriverWait(driver, 600)

    sku_field = waitsku.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/a[1]/div[2]/div/div[1]/div/div/div/div/div/div[1]/div[2]')))

    for i in range(1,loopround):
        sku = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/a[' + str(i) + ']/div[2]/div/div[1]/div/div/div/div/div/div[1]/div[2]')

        print(sku.text)

    sku = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/a[1]/div[2]/div/div[1]/div/div/div/div/div/div[1]/div[2]').text

    JP_sku = 'INS_230109_00095'

    # Parameter
    ## parameter-login
    username = "op_sawamura"
    mycode = "gracesawamura"

    print("[UPDATE] Gracekaitori System")

    ## Login 
    driver.get("https://gracekaitori.com/index.php")
    driver.find_element(By.NAME, "uid").send_keys(username)
    driver.find_element(By.NAME, "pwd").send_keys(mycode)
    driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
    print("[Login] Gracekaitori Successfully")
    time.sleep(1)
    driver.get("https://gracekaitori.com/stocklist.php")
    time.sleep(1)
    driver.find_element(By.NAME, "q").send_keys(JP_sku)
    driver.find_element(By.CSS_SELECTOR, "i[class=\"icon-search\" i]").click()
    driver.close()

    url_line = 'https://notify-api.line.me/api/notify'
    token = 'xMeOA5w8PPaGrIUXrCqAfh7BBg2jz4sd1czAmqdkgx5'
    headers = {'content-tpye': 'application/x-www-form-urlencoded',
               'Authorization': 'Bearer '+token}
    msg = "[UPDATE] Gracekaitori System"
    resp_line = requests.post(
        url_line, headers=headers, data={'message': msg})

submit_button.config(command=submit_input)

window.mainloop()

## Convert DATE (DD/MM/YYYY) to (YYYY-MM-DD)
# DateSold_web = []

# if JP_sku is not None:
#     
#     ## parameter-item
#     item_japan_sku = JP_sku
#     itemprice = itemprice_yen[i]
#     date_sold = DateSold_web[i]
# 
#     if itemprice != '' :
#         ## Go to soldlist
#         time.sleep(1)
#         driver.get("https://gracekaitori.com/stocklist.php")
# 
#         ## Point and Click query
#         time.sleep(1)
#         driver.find_element_by_name("q").send_keys(item_japan_sku)
#         driver.find_element_by_css_selector("i[class=\"icon-search\" i]").click()
# 
#         try:
#             ## Check exist data
#             check_cost_exist = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/table/tbody/tr[8]/td[5]").text
#             if check_cost_exist == "0":
#                 
#                 ## Edit status
#                 time.sleep(1)
#                 driver.find_element_by_css_selector("img[src=\"./images/btnedit.jpg\" i]").click()
# 
#                 ## Fill form
#                 time.sleep(1)
#                 driver.find_element_by_name("itemprice").send_keys(itemprice)
#                 driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/table/tbody/tr[17]/td/input[2]").click()
#                 driver.find_element_by_name("solddate").send_keys(date_sold)
#                 driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/table/tbody/tr[23]/td/input[8]").click()
#                 
#                 
#                 ## Submit update
#                 driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/table/tbody/tr[29]/td").click()
# 
#                     
#                 ## Confirm 
#                 time.sleep(1)
#                 driver.find_element_by_xpath("/html/body/div[3]/div/button[2]").click()
#                     
# 
#                 print("[OnWebKaitori] item-SKU-Japan update : " + str(SKU_japen[i]) + " successfully" + "\n")
#                 worksheet_CAMERA_SALES_REPORT_2020.update_cell(newitem +1 + i,18,"updated")
#                 format_cell_range(worksheet_CAMERA_SALES_REPORT_2020,"R{}".format(newitem +1 + i),fmt_green_text)
#                 
# 
#             else:
#                 print("[OnWebKaitori] item-SKU-Japan exist : " + str(SKU_japen[i]) + "\n")
#                 worksheet_CAMERA_SALES_REPORT_2020.update_cell(newitem +1 + i,18,"SKU-Japan exist ({})".format(str(SKU_japen[i])))
#                 format_cell_range(worksheet_CAMERA_SALES_REPORT_2020,"R{}".format(newitem +1 + i),fmt_red_text)
# 
#         except:
#             print("[OnWebKaitori] search " + str(SKU_japen[i]) + "not found\n")
#             worksheet_CAMERA_SALES_REPORT_2020.update_cell(newitem +1 + i,18,"search not found ({})".format(str(SKU_japen[i])))
#             format_cell_range(worksheet_CAMERA_SALES_REPORT_2020,"R{}".format(newitem +1 + i),fmt_red_text)
# 
# 
# else:
#     print("[BAD REQ] " + str(str(SKU_thai[i]) + " not have SKU-Japen"+ "\n"))
#     worksheet_CAMERA_SALES_REPORT_2020.update_cell(newitem +1 + i,18,"not have SKU-JP")
#     format_cell_range(worksheet_CAMERA_SALES_REPORT_2020,"R{}".format(newitem +1 + i),fmt_blue_text)