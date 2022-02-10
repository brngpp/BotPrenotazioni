import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import   EdgeChromiumDriverManager
import time
import os

username=''  ##cod della tessera sanitaria
password='' ##cod fiscale
postal_code=''
phone_number=''
dir_photo=r'D:\analisi_foto_video'
browser =webdriver.Edge(r'pathwebdriver')

def start(username,password,postal_code,phone_number,):
    url = 'https://prenotazioni.vaccinicovid.gov.it/cit/#/login'

    browser.get(url)

    time.sleep(40)


    ###################prima pagina########################################
    isLoading=True
    while(isLoading):
        try:
            browser.find_element_by_id("username").send_keys(username)
            isLoading=False
        except:
            time.sleep(2)
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_xpath("/html/body/app-root/div/div[2]/app-login/div/form/div[2]/div/div/label").click()
    browser.find_element_by_xpath("/html/body/app-root/div/div[2]/app-login/div/form/div[3]/div/button[1]/span").click()
    #######################################################################

    ##################seconda pagina#######################################
    isLoading = True
    while (isLoading):
        try:
            browser.find_element_by_id("postalCode").send_keys(postal_code)
            isLoading = False
        except:
            time.sleep(2)
    browser.find_element_by_id("phoneNumber").send_keys(phone_number)
    browser.find_element_by_xpath("/html/body/app-root/div/div[2]/app-new-booking/app-new-booking-search/div/form/div[3]/div/div/label").click()

    bool=True
    while(bool):
        try:
            element=browser.find_element_by_xpath("/html/body/app-root/div/div[2]/app-new-booking/app-new-booking-search/div/form/div[5]/div/button[1]/span")
            time.sleep(5)
            element.click()
        except:
            time.sleep(10)
            browser.maximize_window()
            browser.save_screenshot('FullPageScreenshot.png')
            browser.close()
            bool=False
    browser.close()

def stop():
    browser.close()
