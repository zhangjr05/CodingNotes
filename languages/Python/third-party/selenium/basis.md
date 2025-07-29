# Selenium

---

```python
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# 设置正确驱动路径，创建 WebDriver 对象
service = Service(executable_path='D:/tools/msedgedriver.exe')  # 已将其放在系统路径中或 py 目录下可省略
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

# 调用 get 方法，让浏览器打开指定网址
driver.get('https://www.baidu.com')
time.sleep(2)   # 等待页面加载完成

# 导航
driver.back()       # 后退
driver.forward()    # 前进
driver.refresh()    # 刷新

# 查找页面元素
search_box = driver.find_element('id', 'kw')    # 通过 id 查找元素
search_button = driver.find_element("class name", "s_ipt")  # 通过类名查找元素
links = driver.find_elements('tag name', 'a')   # 通过标签查找元素

# 模拟用户操作
search_box.send_keys("南京大学")    # 在搜索框中输入文本
search_button.click()   # 点击搜索按钮

# 获取元素文本和属性
element_text = search_box.text  # 获取元素的文本
element_attribute = search_box.get_attribute("placeholder") # 获取元素属性值

# 等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 显式等待
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "kw")))

# 隐式等待
driver.implicitly_wait(10)

# 关闭浏览器
driver.quit()
```

---

## 元素定位

```python
# 单个元素定位
driver.find_element(By.ID, "id_value")          # 通过 id 定位
driver.find_element(By.NAME, 'name_value')      # 通过 name 定位
driver.find_element(By.CLASS_NAME, "class_name") # 通过 class name 定位
driver.find_element(By.TAG_NAME, "tag_name")    # 通过标签定位

# 过时方法例子
driver.find_element_by_id("element_id")
driver.find_element_by_name("element_name")
driver.find_element_by_class_name("element_class")
driver.find_element_by_tag_name("tag_name")

# 多个元素定位
driver.find_elements(By.TAG_NAME, "tag_name")  # 定位多个元素，返回列表
```

---

## 常用方法

```python
send_keys()       # 输入文本
click()           # 点击
clear()           # 清空输入框
get_attribute()   # 获取元素属性值
element.text      # 获取元素文本内容
```
