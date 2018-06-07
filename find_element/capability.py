from  appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62025'
desired_caps['platforVersion']='5.1.1'
desired_caps['automationName']='uiautomator2'

desired_caps['app']=r'C:\Users\Shuqing\Desktop\kaoyan3.1.0.apk'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

desired_caps['noReset']='False'
desired_caps['unicodeKeyboard']="True"
desired_caps['resetKeyboard']="True"


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(2)


def check_cancelBtn():
    print('check cancelBtn')

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    print('check skipBtn')

    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()
# check_skipBtn()


