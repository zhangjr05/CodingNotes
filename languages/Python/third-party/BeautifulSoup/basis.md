# BeautifulSoup

---

```python
import re
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}

url = 'https://github.com/zhangjr05/Projects'
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'  # 确保正确编码

# 创建 BeautifulSoup 对象，将 HTML 字符串转为 BeautifulSoup 对象
soup = BeautifulSoup(response.text, 'lxml')  # 使用 lxml 解析器，速度快且容错能力强
```

---

## 基本元素选择方法

- **直接访问标签**

    ```python
    title = soup.title  # 获取标题
    print(title)   # <title>Projects of zhangjr05</title>
    print(title.string)    # Projects of zhangjr05
    ```

    ```python
    p = soup.p
    print(p)   # <p class="intro">这是一个很好的库</p>
    ```

- **使用 `find` 和 `find_all` 方法**

    ```python
    first_a = soup.find('a')  # 查找第一个匹配的元素
    print(first_a)  # <a href="https://github.com/zhangjr05/Projects">click here</a>
    first_a.get('href')  # 获取 href 属性的值
    ```

    ```python
    all_links = soup.find_all('a')  # 查找所有匹配的元素
    for link in all_links:
        link.get('href')  # 获取所有 a 元素的 href 属性值
    ```

- **按属性查找**

    ```python
    intro_p = soup.find('p', class_='intro')  # 查找 class 为 intro 的 p 元素
    intro_p.text  # 这是一个很好的库
    ```

- **使用多个条件**

    ```python
    result = soup.find_all('div', attrs={'id': 'content', 'class': 'main'})
    ```

- **CSS 选择器(select)**

    ```python
    links = soup.select('a')  # 选择所有 a 标签
    intro = soup.select('p.intro')  # 选择 class 为 intro 的 p 元素
    header = soup.select('div#header')  # 选择 ID 为 header 的 div 元素
    items = soup.select('ul.menu > li')  # 选择 ul.menu 的直接子元素 li
    ```

---

## 导航文档树

- **获取父节点**

    ```python
    parent = soup.a.parent
    parents = soup.a.parents
    ```

- **获取子节点**

    ```python
    children = soup.body.children
    ```

- **兄弟节点**

    ```python
    next_sibling = soup.p.next_sibling  # 下一个兄弟节点
    prev_sibling = soup.p.previous_sibling  # 上一个兄弟节点
    siblings = soup.p.next_siblings  # 所有兄弟节点
    ```

---

## 获取内容和属性

```python
text = soup.p.text  # 获取文本内容
all_text = soup.get_text()  # 获取标签内所有文本（包括子标签）
href = soup.a['href']  # 获取属性值
attrs = soup.a.attrs  # 获取所有属性，返回字典
soup.p.has_attr('class')  # 检查是否存在某个属性
```

---

## 高级技巧

- **正则表达式**

    ```python
    p_zhangjr = soup.find_all('p', string=re.compile('zhangjr'))  # 查找所有包含 'zhangjr' 的 p 元素
    http_links = soup.find_all('a', href=re.compile('^http'))  # 查找所有以 http 开头的链接
    ```

- **自定义过滤函数**

    ```python
    long_paragraphs = soup.find_all('p', string=lambda text: text and len(text) > 50)  # 查找所有长度大于 50 的段落
    has_multiple_classes = soup.find_all(lambda tag: tag.has_attr('class') and len(tag.get('class')) > 1)  # 查找所有包含多个类的元素
    ```

- **递归限制**

    ```python
    direct_divs = soup.find_all('div', recursive=False)  # 只搜索直接子元素，不递归搜索
    ```
