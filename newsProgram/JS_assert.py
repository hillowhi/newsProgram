# excepted = "你好"
# reality = "你好1"
# # assert excepted == reality, "断言失败"
# assert excepted == reality, '{0}！= {1}'.format(excepted, reality)
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.set_window_size(200, 800)

driver.get("https://broker-dev.mklij.com/login")
driver.find_element("xpath", """//span[text()="密码登录"]""").click()
driver.find_element("xpath", """//input[@placeholder="请输入工号"]""").send_keys("012682")
driver.find_element("xpath", """//input[@placeholder="请输入密码（身份证后6位）"]""").send_keys("123456")
driver.find_element("xpath", """//span[text()="登录"]""").click()
assert driver.find_element("xpath", """//a//span[text()="首页"]"""), "登陆失败！"
driver.switch_to.new_window("tab")
driver.get("https://broker-dev.mklij.com/fangyuan/fangyuan/sell")
driver.execute_script("window.scrollTo(200,1000)")

# driver.find_element()
