from find_element.capability import driver

driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('zxw1234')

driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @index="3"]').send_keys('zxw123456')

# driver.find_element_by_xpath('//android.widget.Button').click()

driver.find_element_by_xpath('//*[@class="android.widget.Button"]').click()