from cmath import log
from curses import init_pair
from lib2to3.pgen2 import driver
from pickle import TRUE
import time
import unittest
import click
from matplotlib.pyplot import get
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import csv
from selenium.webdriver.common.keys import Keys
import os

#def getKyTuDacBIet():
#    return '(#^!$!)#*'

def getElement(driver, xpath):
    try:
        return driver.find_element(by=By.XPATH,value=xpath)
    except:
        return None

def removeText(driver, xpath, sleep = 0.5):
    try:
        el = driver.find_element(by=By.XPATH,value=xpath)
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.DELETE)
    except:
        pass
    finally:
        time.sleep(sleep)

def fillText(driver, xpath, text):
    try:
        el = getElement(driver, xpath)
        el.send_keys(text)
        return el
    except:
        return None
    
def clearAndFillText(driver, xpath, text):
    removeText(driver, xpath)
    fillText(driver, xpath, text)
    

def handleClick(driver, xpath, sleep = 1):
    try:
        driver.find_element(by=By.XPATH,value=xpath).click()
    except:
        pass
    finally:
        time.sleep(sleep)
    
def handleClickOrDefault(driver, xpath, xpathDefault, sleep = 1):
    try:
        try:
            driver.find_element(by=By.XPATH,value=xpath).click()
        except:
            driver.find_element(by=By.XPATH,value=xpathDefault).click()
    except:
        pass
    finally:
        time.sleep(sleep)

class SimpleTest(unittest.TestCase):
    domain = "https://dev.api.crypto.mobilelab.vn"
    domainWithdraw = "https://dev.api.crypto.mobilelab.vn/user/wallet/withdrawal?coin=TRUSTK"
    linkVCN  = "//div[normalize-space()='Ví cá nhân']"
    btnRutTK = "//a[@href='/user/wallet/withdrawal?coin=TRUSTK']"
    xpathInputDiaChi = "//input[@type='text']"
    xpathChain = "//div[@class='ant-select ant-select-lg uppercase ant-select-single ant-select-show-arrow']//div[@class='ant-select-selector']"
    xpathDefaultChainChooseBEP20 = "//div[contains(text(),'bep20')]"
    xpathTemplateChainChooseBEP20 = "//div[contains(text(),'{0}')]"
    xpathAmount = "//input[@role='spinbutton']"
    xpathWithdrawBtn = "//button[@class='ant-btn ant-btn-default receive-button']"
    xpathConfirmBtn = "//button[@class='ant-btn ant-btn-primary']"
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.domain)

        with open('session.txt') as f:
            session = f.read()
            print(session)
            script_session = "window.localStorage.setItem('session',`{0}`);".format(session)
            self.driver.execute_script(script_session)
        # self.driver.refresh()
        self.driver.get(self.domainWithdraw)
        time.sleep(5)

    def handleSearchTxT(self, element, keySearch):
        print('handleSearchTxT')
        element.send_keys(keySearch)

        time.sleep(2)
        emptyEl = getElement(self.driver, self.emptyImgEl)

        if emptyEl is None:
            packagesEl = self.driver.find_elements(by=By.XPATH, value=self.packageEl)
            print(packagesEl.__len__())
            for i in range(packagesEl):
                self.assertTrue(keySearch in packagesEl[i].text, "result not contain search string")
                
    def testRut(self):
        
        try:
            addrIndex = 0
            chainIndex = 1
            amountIndex = 2
            with open('TestcaseRut.csv', 'r') as fileRut:
                reader = csv.reader(fileRut)
                for data in reader:
                    print(data)
                    addr = data[addrIndex]
                    chain = data[chainIndex].strip()
                    amount = data[amountIndex]

                    clearAndFillText(self.driver, self.xpathInputDiaChi, addr)
                    handleClick(self.driver, self.xpathChain)
                    handleClickOrDefault(self.driver, self.xpathTemplateChainChooseBEP20.format(chain), self.xpathDefaultChainChooseBEP20)
                    time.sleep(1)
                    clearAndFillText(self.driver, self.xpathAmount, amount)
                    time.sleep(1)
                    handleClick(self.driver, self.xpathWithdrawBtn)
                    handleClick(self.driver, self.xpathConfirmBtn)
                    time.sleep(3)
                    
                    # viet test case vào đây
                    
            
        except Exception as ex:
            print(ex)
            
if __name__ == '__main__':
       unittest.main()
            
