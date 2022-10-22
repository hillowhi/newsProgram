# excepted = "你好"
# reality = "你好1"
# # assert excepted == reality, "断言失败"
# assert excepted == reality, '{0}！= {1}'.format(excepted, reality)
from selenium import webdriver

# driver = webdriver.Chrome()
# driver.implicitly_wait(2)
# driver.set_window_size(200, 800)
#
# driver.get("https://broker-dev.mklij.com/login")
# driver.find_element("xpath", """//span[text()="密码登录"]""").click()
# driver.find_element("xpath", """//input[@placeholder="请输入工号"]""").send_keys("012682")
# driver.find_element("xpath", """//input[@placeholder="请输入密码（身份证后6位）"]""").send_keys("123456")
# driver.find_element("xpath", """//span[text()="登录"]""").click()
# assert driver.find_element("xpath", """//a//span[text()="首页"]"""), "登陆失败！"
# driver.switch_to.new_window("tab")
# driver.get("https://broker-dev.mklij.com/fangyuan/fangyuan/sell")
# driver.execute_script("window.scrollTo(200,1000)")
# driver.find_element()

# 将定位元素展示在控制大小的窗口里
# driver = webdriver.Chrome()
# driver.set_window_size(200, 800)
# driver.get("https://baijiahao.baidu.com/s?id=1747310370127918629&wfr=spider&for=pc")
# el = driver.find_element("xpath", """//span[text()="举报/反馈"]""")
# js = "arguments[0].scrollIntoView()"
# driver.execute_script(js, el)
# nice！(๑•̀ㅂ•́)و✧

# 修改元素文本信息 or 获取文本信息
# js = "arguments[0].innerHTML='随便举报！我不怕'"
# 引号层级 比如最外层是“” 那么里层不能用“”“ ”“” 只能用‘ ’ 或者 “” “”
# driver.execute_script(js, el)
# js = "return arguments[0].innerHTML"
# text = driver.execute_script(js, el)
# print(text)

# 获取元素属性值
# el2 = driver.find_element("xpath", """//h3[@class="index-module_recentArticleTitle_1t2-a"][1]""")
# js = "return arguments[0].getAttribute('title')"
# text = driver.execute_script(js, el2)
# print(text)

# keys类应用
from selenium.webdriver import Keys

# from selenium.webdriver.common import keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element("id", "kw").send_keys("周杰伦")
driver.find_element("id", "kw").send_keys(Keys.ENTER)
driver.implicitly_wait(2)
# 不加等待会报错
driver.find_element("id", "kw").send_keys(Keys.CONTROL, "a")
