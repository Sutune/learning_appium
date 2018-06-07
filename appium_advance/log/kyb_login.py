from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException
import logging
import logging.config


CON_LOG='../log/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


stream=open('../yaml/desired_caps.yaml','r')
data=yaml.load(stream)

desired_caps={}
desired_caps['platformName']=data['platformName']

desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']

desired_caps['app']=data['app']
desired_caps['noReset']=data['noReset']

desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
desired_caps['resetKeyboard']=data['resetKeyboard']

desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']

driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)

def check_updateBtn():
    logging.info("check_updateBtn")

    try:
        element = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info('update element is not found!')
    else:
        element.click()


def check_skipBtn():
    logging.info("check_skipBtn")
    try:
        element = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info('skipBtn element is not found!')
    else:
        element.click()

check_updateBtn()
check_skipBtn()

logging.info('start login...')

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('自学网2018')
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
logging.info('login finished')
