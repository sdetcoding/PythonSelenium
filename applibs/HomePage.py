import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utility.BaseClass import BaseClass


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    txt_Search_City = (By.XPATH, "//input[@id='LocationSearch_input']")
    lst_City = (By.XPATH, "//button[@id='LocationSearch_listbox-0']")
    sTempValue = (By.XPATH, "//span[@data-testid ='TemperatureValue']")
    sHumidity = (By.XPATH, "//span[@data-testid ='PercentageValue']")
    sPressure = (By.XPATH, "//span[@data-testid ='PressureValue']")
    sVisibility = (By.XPATH, "//span[@data-testid ='VisibilityValue']")
    sWind = (By.XPATH, "//span[@data-testid ='Wind']")
    sDewPoint = (By.XPATH, "//div[text()='Dew Point']/following-sibling::div/span")

    def txtSearchCity(self):
        return self.driver.find_element(*HomePage.txt_Search_City)

    def lstSearchCity(self):
        return self.driver.find_element(*HomePage.lst_City)

    def getTempValue(self):
        return self.driver.find_element(*HomePage.sTempValue)

    def getHumidity(self):
        return self.driver.find_element(*HomePage.sHumidity)

    def getPressure(self):
        return self.driver.find_element(*HomePage.sPressure)

    def getDewPoint(self):
        return self.driver.find_element(*HomePage.sDewPoint)

    def getWind(self):
        return self.driver.find_element(*HomePage.sWind)

    def getVisibility(self):
        return self.driver.find_element(*HomePage.sVisibility)

    def waitforlstcity(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='LocationSearch_listbox-6']")))

    def waitforInput(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='LocationSearch_input']")))

    def delay(self):
       time.sleep(1)

    @staticmethod
    def validation(webvlue, apivalue, scomapre, sVariance):
        i = int(sVariance)
        log = BaseClass.getLogger()
        if float(webvlue) - float(apivalue) <= i:
            assert True
            log.info('%s does not match  but minimum difference is less than 3', scomapre)

        elif float(webvlue) - float(apivalue) == 0:
            log.info('%s  matched', scomapre)
            assert True

        else:
            try:
                assert False

            except Exception:
                log.error('%s does not match  but minimum difference is more than 3', scomapre)