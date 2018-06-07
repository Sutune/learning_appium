from find_element.capability import driver
from time import sleep

def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y

l=get_size()
print(l)

def swipeLeft():
    l=get_size()
    x1=int(l[0]*0.9)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.95)
    y2 = int(l[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)

def swipeDown():
    l=get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.35)
    y2 = int(l[1] * 0.85)
    driver.swipe(x1, y1, x1, y2, 1000)

def swipeRight():
    l=get_size()
    y1 = int(l[1] * 0.5)
    x1 = int(l[0] * 0.25)
    x2 = int(l[0] * 0.95)
    driver.swipe(x1, y1, x2, y1, 1000)

if __name__ == '__main__':

    for i in range(2):
        swipeLeft()
        sleep(0.5)

    driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()