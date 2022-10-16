from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://music.163.com')
sleep(2)
driver.find_element('xpath', """//*[@hidefocus="true" and text() = '登录']""").click()
sleep(1)
driver.find_element('xpath', "//*[text() = '选择其他登录模式']").click()
sleep(1)
driver.find_element('xpath', "//*[@type='checkbox']").click()
driver.find_element('xpath', "//*[text() = 'QQ登录']").click()
sleep(2)
driver.switch_to.window(handles[1])
# 需要将selenium 升级到4版本
driver.find_element("xpath", "//*//input[@id='select_all']")

"""
:Usage:
            ::

                driver.switch_to.frame('frame_name')
                driver.switch_to.frame(1)
                driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
       
       //*[@id ='ptlogin_iframe']
"""


driver.switch_to.frame(driver.find_element('tag name', "frame")[0])
driver.find_element('xpath', "//*[text()='密码登录' and @ id ='switcher_plogin']").click()

