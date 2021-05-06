from appium import webdriver

desired_caps = {
    "deviceName": "punit",
    "platformName": "Android",
    "platformVersion": "11.0",
    "app": "<url >"

}


class Test:

    def test_01(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        eLauncher = driver.find_element_by_xpath("*//android.widget.TextView[@Text='game.tv']")
        assert eLauncher.is_displayed(), " App install not successful"
        eLauncher.click()
        stwitterimg = driver.find_element_by_xpath("*//android.widget.ImageView[@index='2']")
        assert stwitterimg.is_displayed(), "twitter image is not displayed"
        stwitterimg.click()
        driver.find_elements_by_id("username_or_email").send_keys("test1.auto1@gmail.com")
        driver.find_elements_by_id("password").send_keys("game@twitter")
        driver.find_elements_by_id("allow").click()
        assert not driver.find_elements_by_id("challenge_response"), "Not successfully logon"
