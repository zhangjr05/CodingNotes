# 文件操作

---

## 打开文件，四种模式：'r', 'w', 'a', 'b'

```python
f = open('file.txt', 'r', encoding='utf-8')
f.close()   # 关闭文件
with open('file.txt', 'a', encoding='utf-8') as f:
    pass
```

---

## 文件读取

```python
f.read(size=-1) # 读取全部内容
f.readline(size=-1) # 逐行读取，含换行符
f.readlines(hint=-1)    # 读取所有行，返回list
```

---

## 文件写入

```python
f.write(s='Hello, world!')  # 写入字符串
f.writelines(lines=['Hello\n', 'World\n'])  # 写入字符串列表，不自动换行
f.flush()   # 强制刷新缓冲区内容到磁盘
```
