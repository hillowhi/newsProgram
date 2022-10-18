###三类等待机制：
>time.sleep 强制等待 sleep(5)

>driver.implicity_wait(5) 隐式等待 driver对象的设置项 只对当前的driver有效 driver.quite()后失效
> 设置后的代码生效 在页面加载完成后如果没有查找到元素 则触发等待 平均0.5S一次 如果最大等待时间没有找到元素不会返回错误信息 代码继续运行

>显示等待 el = WebDriverWait(driver, 5,0.5).until(lambal el:driver.find_element('xpath', ''), message="显示等待失败咯！")

>until表示对指定的元素进行等待 查找成功则返回该元素，失败 则返回message信息 抛出TimeoutException

>until_not表示指定的元素进行等待消失 如果在最大等待时间内该元素小时，成功！ 则返回true 并抛出message信息 如果元素一直存在 则返回false

>显示等待和隐式等待一起用的时候 以等待时间长的为准

### 页面缓存加载机制：
> driver浏览器自行启动的页面是不会加载已有的页面缓存的 selenium提供了一些可以加载cookie策略 
> 1.默认加载策略：nomal
> 2.放弃加载静态资源和css样式：eager
> 3.等待初始页面加载完成就直接操作 不考虑其他内容：none

eg:options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager' #设置页面加载策略
driver = webdriver.Chrome()
driver.get(“http://baidu.com”)





