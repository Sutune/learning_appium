from  appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62025'
desired_caps['platforVersion']='5.1.1'

# desired_caps['deviceName']='MX4'
# desired_caps['platforVersion']='5.1'
# desired_caps['udid']='750BBKL22GDN'


desired_caps['app']=r'C:\Users\Shuqing\Desktop\kaoyan3.1.0.apk'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id('android:id/button2').click()
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()



