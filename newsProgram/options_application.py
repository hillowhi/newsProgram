from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from newsProgram.chrome_options import options

# 引用chrome_options里封装好的options方法

driver = webdriver.Chrome(options=options())
driver.get('https://broker-dev.233.com/login')
sleep(2)
driver.find_element("xpath", "//div[@class ='change-login']").click()
sleep(1)
driver.find_element('xpath', '//input[@placeholder="请输入工号" and @class="el-input__inner"]').send_keys("012666")
driver.find_element('xpath', '//input[@type="password" and @class="el-input__inner"]').send_keys("123456")
driver.find_element('xpath',
                    '//button[@type="button" and @class="el-button el-button--primary el-button--small"]').click()
sleep(3)
driver.switch_to.new_window('tab')

driver.get("https://broker-dev.mklij.com/fangyuan/fangyuan/detail/1929409?type=sell")
sleep(12)
driver.find_element('xpath', """//div[@class='house-title']/span[2]/button[1]""").click()
"""
用斜杠的方法获取子元素很好用！！！奈斯(๑•̀ㅂ•́)و✧
"""
# collect_button_text = driver.find_element('xpath', """//div[@class='house-title']/span[2]/button[1]""").text()
# assert '已收藏' == collect_button_text, '加入成功 != {}.format(collect_button_text)'

"""
定位元素是否出现 用assert不太好 最好用显示等待 但是同一个元素 只是改变了文本内容 所以用assert比较方便
"""
WebDriverWait(driver, 5, 0.5).until(driver.find_element('xpath', """//div[@class='house-title']/span[2]/button[1]"""),
                                    message="收藏失败")
