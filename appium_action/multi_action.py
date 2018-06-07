from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62025'
desired_caps['platforVersion']='5.1.1'

desired_caps['app']=r'C:\Users\Shuqing\Desktop\com.baidu.BaiduMap.apk'
desired_caps['appPackage']='com.baidu.BaiduMap'
desired_caps['appActivity']='com.baidu.baidumaps.WelcomeScreen'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

x=driver.get_window_size()['width']
y=driver.get_window_size()['height']

driver.find_element_by_id('com.baidu.BaiduMap:id/dj2').click()
driver.find_element_by_id('com.baidu.BaiduMap:id/byo').click()


def pinch():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    pinch_action=MultiAction(driver)

    action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8,y=y*0.8).wait(1000).move_to(x=x*0.6,y=y*0.6).wait(1000).release()

    pinch_action.add(action1,action2)
    print('start pinch...')
    pinch_action.perform()

def zoom():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
    action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()

    zoom_action.add(action1,action2)
    print("start zoom...")
    zoom_action.perform()

if __name__ == '__main__':
    for i in range(3):
        pinch()

    for i in range(3):
        zoom()


