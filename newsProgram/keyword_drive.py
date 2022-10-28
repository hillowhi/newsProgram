'''
关键字驱动 封装常态化流程
例：封装一个关键字驱动类：
'''
import time

from selenium.webdriver.chrome import webdriver


# 定义多样化浏览器驱动类型
def open_browser(type_):
    # if type_ == "chrome":
    #     driver = webdriver.Chrome()
    # elif type_ == 'firefox':
    #     driver = webdriver.Firefox()
#换用反射机制写法：
    '''
    getattr(webdriver, type_)()
    获取webdriver的type_属性  =  webdriver.type_
    即  webdriver.Chrome
    () 的意思就是返回的是一个函数
    即  webdriver.Chrome()
    '''
    try:
        driver = getattr(webdriver, type_)()

class KeyWord:
    driver = webdriver.Chrome()

    def __init__(self, type_):
        # 定义一个构造函数
        self.driver = open_browser(type_)
        self.driver.implicity_wait(10)

    # 考虑到适配浏览器多样性

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 定位元素 一定要加返回结果！！！！返回定位元素
    def location(self, by, value):
        return self.driver.find_element(by, value)

    # 输入

    def input(self, by, value, txt):
        self.location(by, value).send_keys(txt)

    # 点击

    def click(self, by, value):
        self.location(by, value).click

    # 关闭浏览器

    def quite(self):
        self.driver.quite()

    # 强制等待

    def wait(self, time_):
        time.sleep(time_)
