"""
selenium2 options是通过chrome_options参数传入
selenium3种 options是基于options参数传入
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


# 基于不同的浏览器可以封装Browser_options()根据入参不同调用不同的options()方法

# def Browser_options(browser):
#     if browser == 'chrome':
#         return options()
#     elif browser == 'firefox':
#         return options2()


def options():
    options = webdriver.ChromeOptions()
    # options.page_load_strategy = "normal"
    # options.add_argument('__headless')
    # options.add_argument("start_maximized")
    # 设置页面最大化
    options.add_argument("start_maximized")
    # 浏览器的无头模式
    # options.add_argument('__headless')
    options.add_argument(r'C:\Users\lenovo\AppData\Local\Google\Chrome\User Data\Default')
    # 设置页面位置
    options.add_argument('window_position=1000,1000')
    # 设置页面大小 参数里面 一定不要留空格 会出现奇怪的错误！！！(~_~)
    # options.add_argument('window_size=800,500')
    # 去掉自动化控制警告：
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    return options


def options2():
    return options2


'''  
    火狐浏览器options浏览器设置
'''

# driver.get("https://www.jd.com/")
# driver.find_element("xpath", """//input[@id = "key"]""").send_keys("iphone14pro")
# driver.find_element("xpath", """//button[@aria-label="搜索"]""").click()
# driver.implicitly_wait(2)
# driver.find_element("xpath", """//a[@class="p-o-btn addcart"]""").click()
# driver.find_element("xpath", """//a[text()="账户登录"]""").click()
# driver.find_element("id", "loginname").send_keys("15224***566")
# driver.find_element("id", "nloginpwd").send_keys("huan")
# driver.find_element("id", "loginsubmit").click()
# # 验证码
# driver.find_element("xpath", """//a[text()="我的购物车"]""").click()
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com/")
# ActionChains(driver).move_to_element(driver.find_element("xpath", """//a[text()='我的京东']"""))
# driver.save_screenshot('jingdong2.png')
# a = driver.title
# print(a)
# driver.quit()

