# string 字符串

## basis

- `a = 'hello world i love you'`
- `a.capitalize()`: **第一个字符大写**
- `a.title()`: **单词首字母大写**
- `a.upper()`
- `a.lower()`
- `a.count(str='l', start=0, end=len(a))`: **计数**
- `a.find(str='l', start=0, end=len(a))`: **查找，返回索引，未找到返回-1**
- `a.index(str='l', start=0, end=len(a))`: **同上，未找到则报错**
- `a.rfind()`: **反向查找**
- `a.rindex()`
- `a.split()`: **做切割返回list**
- `a.replace(old='i', new='I', count=-1)`: **count：允许替换的最多个数，默认-1全部替换**
- `'-'.join(a)`: **以'-'作分隔符，返回字符串**
- `a.strip(chars=None)`: **除首尾**
- `a.lstrip()`: **除首**
- `a.rsplit()`: **除尾**
- `a.center(width=40, fillchar=' ')`: **居中**
