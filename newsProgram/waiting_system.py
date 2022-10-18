from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
options = webdriver.ChromeOptions
options.page_load_strategy = "none"
# driver.get("https://broker-dev.nihao.com/broker-api/haha/swagger-ui.html#!/234542120826381921153255090001475"
#            "/deleteVideoUsingGET")
# driver.switch_to.new_window("window")
driver.get("https://image.baidu.com/search/albumsdetail?tn=albumsdetail&word=%E8%88%AA%E6%8B%8D%E5%9C%B0%E7%90%83%E7"
           "%B3%BB%E5%88%97&fr=albumslist&album_tab=%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90&album_id=312&rn=30")
# sleep(2)
# driver.implicitly_wait(2)
element = WebDriverWait(driver, 2, 0.5).until(lambda el: driver.find_element('xpath', """//span[text() ="查看更多合辑"]"""), message="阿尼哈赛呦")
driver.find_element('xpath', """//span[text() ="查看更多合辑"]""").click()
print(element)
print(driver.title)
driver.close()
