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

class SimpleTest(unittest.TestCase):
    domain = "https://dev.api.crypto.mobilelab.vn/staking"
    showStakeInfoBtnEl = "(//button[@type='button'])[2]"
    searchInputEl = "//input[@type='text']"
    emptyImgEl = "//div[@class='ant-empty-image']"
    clearEl = "//span[@aria-label='close-circle']"
    packageEl = "//td[@class='ant-table-cell']//span[@class='pl-small']"
    keySearch = "USDT"
    

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

    def testStaking(self):
        ## click vào staking
        try:
            time.sleep(2)
            element = getElement(self.driver, self.searchInputEl)
                # do it N time
            with open('testcase.csv', 'r') as file:
                reader = csv.reader(file)
                for keySearch in reader:
                    handleClick(self.driver, self.clearEl)
                    element.send_keys(keySearch)
                    time.sleep(2)
                    emptyEl = getElement(self.driver, self.emptyImgEl)
                    # self.assertEqual(emptyEl.is_displayed(), True, "Failed size is not empty")

                    if emptyEl is None:
                        packagesEl = self.driver.find_elements(by=By.XPATH, value=self.packageEl)
                        
                       # print('asdasdasd@@@#@# ', packagesEl.__len__())
                        if packagesEl.__len__() == 0:
                            continue

                        stakingEl = getElement(self.driver, "//div[@class='staking']")
                        print(packagesEl.__len__(), keySearch[0], ': https://github.com/Sonek-HoangBui/demo-ut/blob/main/unittest/demo.py#L83')
                        stakingEl.screenshot(keySearch[0] +'_'+str(packagesEl.__len__())+'.png')
                        for i in range(packagesEl.__len__()):
                            self.assertTrue(keySearch[0].lower() in packagesEl[i].text.lower(), "result not contain search string")
            
            
           
            # emptyEl = self.driver.find_element(by=By.XPATH, value=self.emptyImgEl)
            
            # # testcase is empty
            # self.assertEqual(emptyEl.is_displayed(), True, "Failed size is not empty")

            # # testcase is failed
            # self.assertEqual(emptyEl.is_displayed(), False, "Is empty")

        except Exception as ex:
            # sleep 5s to retry
            print(ex)
            # element = self.driver.find_element(by=By.XPATH,value=self.showStakeInfoBtnEl)
            # element.click()
        
        #Click vào Stake ngay
        time.sleep(2)
        
        element_script = """ #root > div > div > div > div.App-header > div > div.staking-body > div.table > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button"""
        element_btn = """document.querySelector('#root > div > div > div > div.App-header > div > div.staking-body > div.table > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button').click()"""
        
        #verify input
        
           #input 
        try:
            time.sleep(2)
            element = getElement(self.driver, self.searchInputEl)
                # do it N time
            with open('input.csv', 'r') as file:
                reader = csv.reader(file)
                for keySearch in reader:
                    handleClick(self.driver, self.clearEl)
                    element.send_keys(keySearch)
                    time.sleep(2)
                    emptyEl1 = getElement(self.driver, self.emptyImgEl1)

                    if emptyEl1 is None:
                        packagesEl1 = self.driver.find_elements(by=By.XPATH, value=self.packageEl1)
            
        except Exception:
            inputDK = driver.findElement(by=By.XPATH,value="(/html/body/div[6]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/label/span[1]/input).click()]")
            
        #Click vào Stake ngay
        time.sleep(2)   


if __name__ == '__main__':
   unittest.main()
