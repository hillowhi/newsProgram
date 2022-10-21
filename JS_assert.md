### js断言：
> 断言是一个自动化脚本的结束 所有的自动化操作行为都要有一个结果 assert 判断断言是否通过(excepted == reality)
断言为true 则通过 断言失败 则“断言失败”  

一般元素定位不需要断言 显示等待就可以满足元素的定位查找

assert excepted == reality, "断言失败提示的message"

> 获取元素某个属性值 get_attribute()函数
> href = driver.find_element("link_text", "文本信息啊啊啊").get_attribute("href")

所有js执行内容都是关联document对象的

### 控制页面浏览器窗口大小 
>window.scrollTo(x,y) x控制横向滚动条,y控制纵向滚动条 0顶端  1000表示末尾 

### 将元素聚焦到页面中显示 

el =driver.find_elemnet("","")
>js = "argument[0].scrollIntoView()"
driver.execute_script()