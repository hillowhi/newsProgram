### ChromeOptions类 专门用于Chrome浏览器的 配置浏览器对象 自动化测试中只需要初始化一次

>options.add_argument() 用于操作浏览器常规设置
add_experimental_option() 用于添加浏览器实验性设定

eg：
>设置页面最大化:

options.add_argument("start_maximized")

>设置页面位置:

options.add_argument('window_position=500,600')

>设置页面大小:

options.add_argument('window_size =1000,500')

>去掉自动化控制警告：

options.add_experimental_option('excludeSwitches', ['enable-automation'])

>默认加载浏览器缓存:

查找浏览器缓存路径：chrome://version/

options.add_argument("C:\Users\lenovo\AppData\Local\Google\Chrome\User Data\Default")

>防止记住密码弹框加载

prefs = dict()
prefs['credentials_enable_service'] = False
prefs['profile.password_manager_enable'] = False
options.add_experimental_option('prefs', prefs)

>隐身模式 没有句柄概念 

options.add_argument('incognito')

>去掉控制台多余的log打印

options.add_experimental_option('excludeSwitches', [enable_logging])
options.add_argument('--log_level=3')
options.add_argument('--disable-gpu=3')
options.add_argument('--ignore-certificate_errors=3')

>options类里函数庞大 可以直接封装成函数 给driver调用就好  

