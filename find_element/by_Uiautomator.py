from find_element.capability import driver
#
# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('zxw1234')

# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().text("请输入用户名")').send_keys('zxw1234')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().className("android.widget.EditText")').send_keys('zxw1234')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys('zxw123456')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()