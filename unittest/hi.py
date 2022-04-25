from curses import init_pair
from lib2to3.pgen2 import driver
from pickle import TRUE
import time
import unittest
import click
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import csv
from selenium.webdriver.common.keys import Keys
import os
 

def getElement(driver, xpath):
    try:
        return driver.find_element(by=By.XPATH,value=xpath)
    except:
        return None

def handleClick(driver, xpath):
    try:
        driver.find_element(by=By.XPATH,value=xpath).click()
    except:
        pass
    
def fillText(driver, xpath, text):
    try:
        el = getElement(driver, xpath)
        el.send_keys(text)
        return el
    except:
        return None
    
    
def clearAndFillText(driver, xpath, text):
    fillText(driver, xpath, text)
    
    

class SimpleTest(unittest.TestCase):
    domain = "https://dev.api.crypto.mobilelab.vn/staking"
    xpathStakeNgay = "//button[@ant-click-animating-without-extra-node='false']//span[contains(text(),'Stake ngay')]"
    xpathAmount  = "//input[@id='control-ref_deposit_amount']"
    xpathMax = "//span[@class='input--value-max']"
    xpathCheckBoxDieuKhoan = "//input[@type='checkbox']"
    xpathConfirm = "//span[contains(text(),'Xác nhận')]"
    

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.domain)

        with open('session.txt') as f:
            session = f.read()
            script_session = "window.localStorage.setItem('session',`{0}`);".format(session)
            self.driver.execute_script(script_session)
        self.driver.refresh()
        self.driver.get(self.domain)

    def handleSearchTxT(self, element, keySearch):
        print('handleSearchTxT')
        element.send_keys(keySearch)

        time.sleep(2)
        emptyEl = getElement(self.driver, self.emptyImgEl)
        # self.assertEqual(emptyEl.is_displayed(), True, "Failed size is not empty")

        if emptyEl is None:
            packagesEl = self.driver.find_elements(by=By.XPATH, value=self.packageEl)
            print(packagesEl.__len__())
            for i in range(packagesEl):
                self.assertTrue(keySearch in packagesEl[i].text, "result not contain search string")

        
    def Stake(self):
        try:
            #AmountIndex = 0
            handleClick(self.driver, self.xpathStakeNgay)
            el = getElement(self.driver, self.xpathAmount)
            with open('testcaseStake.csv', 'r') as fileStake:
                reader = csv.reader(fileStake)
                for el in reader:
                    #Amount = dataStake[AmountIndex]  
                    clearAndFillText(self.driver, self.xpathAmount)
                    handleClick(self.driver, self.xpathCheckBoxDieuKhoan)
                    time.sleep(2)
                    handleClick(self.driver, self.xpathConfirm)
                    time.sleep(2)
             
        except Exception as ex:
            print(ex)  


if __name__ == '__main__':
   unittest.main()
