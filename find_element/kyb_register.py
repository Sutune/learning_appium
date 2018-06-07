from find_element.capability import driver
import random

driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()

#头像设置
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
images=driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
images[10].click()

driver.find_element_by_id('com.tal.kaoyan:id/save').click()

#用户名密码邮箱信息填写
username='zxw2018'+'FLY'+str(random.randint(1000,9000))
print('username: %s' %username)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)

password='zxw2018'+str(random.randint(1000,9000))
print('password: %s' %password)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)

email='51zxw'+str(random.randint(1000,9000))+'@163.com'
print('email: %s' %email)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()

#院校选择
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[1].click()
driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[1].click()

#专业选择
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[1].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[2].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[1].click()

#点击进入考研帮
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()