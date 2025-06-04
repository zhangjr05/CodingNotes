# os

---

## 路径操作

```python
current_dir = os.getcwd()  # 获取当前工作目录
abs_path = os.path.abspath(__file__)  # 获取当前脚本绝对路径
parent_dir = os.path.dirname(abs_path)  # 获取上级目录
another_file_path = os.path.join(parent_dir, "homework.txt")  # 获取同级目录下另一个文件的绝对路径
```

---

## 文件和目录操作

```python
os.mkdir('d:/work/demo')  # 创建单层目录
os.makedirs('1/2/3/4/5', exist_ok=True)  # 创建多级目录
os.remove()  # 删除文件
os.rmdir()  # 删除空目录
import shutil  # 导包
shutil.rmtree()  # 删除非空目录及其所有内容
os.rename('old.txt', 'new.txt')  # 重命名
os.path.exists()  # 路径是否存在
```
