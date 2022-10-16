# 断言
# excepted = "登陆成功"
# reality = "登陆成功"
# assert excepted == reality, '{1} !={0}'.format(excepted, reality)
from time import sleep

from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://broker-dev.mklij.com/login')
sleep(2)
driver.find_element("xpath", "//div[@class ='change-login']").click()
sleep(1)
driver.find_element('xpath', '//input[@placeholder="请输入工号" and @class="el-input__inner"]').send_keys("012682")
driver.find_element('xpath', '//input[@type="password" and @class="el-input__inner"]').send_keys("123456")
driver.find_element('xpath',
                    '//button[@type="button" and @class="el-button el-button--primary el-button--small"]').click()
# login_success = WebDriverWait(driver, 3, 0.5).until(
#     EC.presence_of_element_located(('xpath', """//div//p[@class="active" and text()="上海市-严骏区域-物业顾问"]""")))
sleep(1)
driver.find_element('xpath', """//div//p[@class="active" and text()="上海市-严骏区域-物业顾问"]""").click()
sleep(3)
