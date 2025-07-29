# ast

提供更安全的`eval()`

```python
import ast
msg = ast.literal_eval(input())
print(msg)
```

**只接受数字，字符串，列表，元组，字典，集合等。**
