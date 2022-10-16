#### selenium 特定场景下关于浏览器的操作行为：

> driver.title() 获取当前页面的title

> driver.find_element() or driver.find_elements() 获取单个/多个元素

> driver.find_element().send_keys() 可以传文本 也可以传单个文件 如果传入的是文本send_keys('file_url') file_url可以是本地绝对路径，也可以是文件相对路径

> 鼠标操作 类 ActionChains库 用法：ActionChains(driver).move_to_element(driver_find_element('id','')).perform() 等等常见的鼠标操作 悬浮 滚动

> driver.close() & driver.quite() quite 关闭浏览器进程  close() 关闭当前的页面 driver进程还存在 仍然可以调用

> 句柄与frame: 每一个标签页就是一个句柄 多个页面操作就需要句柄之间切换

> driver.get_current_window_handle 获取当前页面句柄  driver.switch_to.window(handles[1]) 获取下一个页面的句柄 即切换页面
> 一般自动化操作最多保留两个页面 打开新的页面后 调用driver.close()方法 关闭当前不需要的页面 再切换到新的句柄

>frame: 定位frame中的元素 需要进入frame 操作元素后 再从frame里退出

> 切换至frame结构 driver.switch_to.frame(frame_name) 退出frame driver.switch_to.default_content()

#### selenium4以上版本支持的操作行为：1.实现多地址个页面打开，实现多个窗口地址页面打开 switch_to.new_window(‘’) 1.tab 2,window 创建新的标签页 句柄会跟随切换 

>driver.get(url1)  **driver.switch_to.new_window('tab')** driver.get(url2) 打开新的地址路径窗口

>driver.get(url1) **driver.switch_to.new_window('window')** driver.get(url2) 通过打开新窗口访问新的地址路径
