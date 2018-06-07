from find_element.kyb_login import driver
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum'))
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()