import pytest

import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        log = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        log.addHandler(fileHandler)
        log.setLevel(logging.DEBUG)
        return log


