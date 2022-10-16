### 抓取地铁数据小结
> 库连接： 
> conn = pymysql.connect(
        host="rm-uf6mav88a70rf99w3to.mysql.rds.aliyuncs.com",
        user="gaohan",
        passwd="GAOhan1234567",
        database="lualu",
        autocommit=True
    )

> if __name__ == "__main__" 
> 调用函数写在 main函数里的优点：防止引用模块在引用时重复调用

>excute(sql,args) 方法 
有两个参数 ，适用于当sql语句包含变量时, args可以是变量,写法官方解释如下：
If args is a list or tuple, %s can be used as a placeholder in the query.
  If args is a dict, %(name)s can be used as a placeholder in the query.

> eg: excute("insert into subway (line,station) values (%s,%s),(r["line"],r["station"])")
> 

*args表示任何多个无名参数，它是一个tuple or list；**kwargs表示关键字参数，它是一个 dict

> xpath 的用法：
id,name,link text,tagname,class name,

id:
>id是独有基本不重复 find.element('id','kw')

name：
> name 可能重复 find.element('name','kw')

tag name:
> 标签名称定位重复性高 find.element('tag name','kw') 可批量获取标签名称相同name的情况，多用于爬虫

class name:
> 基于class属性定位 命明复杂 find.element('tag name','kw')

link text:
>文本标签，只适用于<a>标签 find_element('link text', '新闻')

partial link text:
>模糊匹配链接文本 只适用于a标签 查找多个结果 list，eg：find_elements,或者只查找一个find_element,只拿最开始匹配到的第一个值

xpath:
> // 表示从根路径下开始查找
 
> *表示任意元素

>[]表示添加筛选条件

>@表示元素名称

>= 表示赋
 
>text() 表示文本 文本前有属性值的时候不适用这个方法查找 查找关系支持关系查找 and or contains()表示对内容进行模糊查找 eg: //button[contains(text(),"录“)]
 
>//*[@id='kw']/.. 表示获取id=kw属性的父级元素 适用于父级元素的属性值是随机变化的类型

>//*[@id='s_kw_wrap']/input 表示获取id='s_kw_wrap' 的子元素input


####原点定位selenium4新用法 目前定位结果没多大意义 相对定位器 返回多个值 locate_with() find_element(locate_with(By.TAG_NAME, 'id'))
el = driver,find_element('id', 'kw')
>上 a = driver.find_element(locate_with(By.TAG_NAME, 'div').above(el))
> 下 a = driver.find_element(locate_with(By.TAG_NAME, 'div').below(el))
> 左 a = driver.find_element(locate_with(By.TAG_NAME, 'div').to_left_of(el))
> 右 a = driver.find_element(locate_with(By.TAG_NAME, 'div').to_right_of(el))
> 附近 a = driver.find_element(locate_with(By.TAG_NAME, 'div').near(el))