import json

import requests

from applibs.HomePage import HomePage
from data.BaseData import BaseData
from utility.BaseClass import BaseClass


class Test(BaseClass):

    def test_one(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        if homePage.txtSearchCity().is_displayed():
            log.info(" Welcome to Weather.com")
        for i in BaseData.lsCity:
            homePage.waitforInput()
            homePage.delay()
            homePage.txtSearchCity().click()
            homePage.txtSearchCity().send_keys(i)
            city = i
            log.info('Search City: %s', city)
            log.info('----------%s----------', city)
            homePage.waitforlstcity()
            homePage.delay()
            homePage.lstSearchCity().click()
            homePage.delay()
            tempvalue = homePage.getTempValue().text
            tempv = int(tempvalue[:-1])
            log.info("-----------------------------------")
            log.info('Temperature by Web: %s', tempv)
            windbyweb = homePage.getWind().text
            pressurebyweb = homePage.getPressure().text
            humididtybyweb = homePage.getHumidity().text
            windw = float(windbyweb[:-5])
            pressw = float(pressurebyweb[:-3])
            humidityw = float(humididtybyweb[:-1])
            log.info('wind from web: %s', windw)
            log.info('Pressure from web: %s', pressw)
            log.info('Humidity from web: %s', humidityw)
            log.info("-----------------------------------")

            response = requests.get(
                'https://api.openweathermap.org/data/2.5/weather?q=' + i + '&appid=7e7c713211fd97fdac5e1330070499e9&units=metric')
            rs = json.dumps(response.json())
            js = json.loads(rs)
            x = js['main']
            w = js['wind']
            for key, value in x.items():
                if key == "temp":
                    api_Temp = value
                elif key == "pressure":
                    api_pressure = value
                elif key == "humidity":
                    api_humidity = value
            for key, value in w.items():
                if key == "speed":
                    api_wind = value
            log.info('Temperature by API: %s', api_Temp)
            log.info('Pressure by API: %s', api_pressure)
            log.info('Humidity by API: %s', api_humidity)
            log.info('Wind by API: %s', api_wind)
            log.info("--------------- Validation --------------------")
            homePage.validation(tempv, api_Temp, "Temperature", 3)
            homePage.validation(pressw, api_pressure, "Pressure", 3)
            homePage.validation(humidityw, api_humidity, "Humidity", 3)
            homePage.validation(windw, api_wind, "Wind", 3)
