# Python MRO (Method Resolution Order)

## 核心概念

MRO决定了多重继承中方法和属性的查找顺序，使用**C3线性化算法**。

## 基本示例

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

**查找顺序**: D → B → C → A → object

## C3算法核心规则

1. **子类优先于父类**
2. **左侧父类优先于右侧父类**
3. **保持父类间的相对顺序**

## 复杂继承

```python
class A:
    def method(self): print("A")

class B(A):
    def method(self): 
        print("B")
        super().method()

class C(A):
    def method(self): 
        print("C")
        super().method()

class D(B, C):
    def method(self):
        print("D")
        super().method()

# MRO: D → B → C → A
# 关键：C会调用A，而不是跳过
D().method()
# 输出: D, B, C, A
```

## MRO计算规则详解

### C3线性化算法步骤

**公式**: `L(C) = C + merge(L(B1), L(B2), ..., L(BN), B1B2...BN)`

- `C` 是要计算MRO的类
- `B1, B2, ..., BN` 是C的直接父类
- `L(X)` 表示类X的MRO
- `merge` 是合并操作

### merge操作规则

1. **取头规则**：从第一个非空列表取头元素
2. **检查尾规则**：该元素不能出现在其他列表的尾部（除非也是头部）
3. **冲突处理**：如果冲突，尝试下一个列表
4. **移除规则**：选中元素后，从所有列表中移除该元素

### 手工计算示例

```python
class A: pass
class B(A): pass  
class C(A): pass
class D(B, C): pass

# 计算步骤：
# L(A) = [A]
# L(B) = B + merge([A], [A]) = [B, A]
# L(C) = C + merge([A], [A]) = [C, A]

# L(D) = D + merge([B,A], [C,A], [B,C])
#      = D + merge([B,A], [C,A], [B,C])  # 取B: B是第一个列表头，且不在其他列表尾部
#      = [D,B] + merge([A], [C,A], [C])   # 取C: C是第二个列表头，且不在其他列表尾部  
#      = [D,B,C] + merge([A], [A], [])    # 取A: A是头部且所有列表都有
#      = [D,B,C,A]
```

## 树形理解MRO

**将继承关系看作树，MRO就是从叶节点开始，按层级从左到右的遍历顺序。**

```markdown
从底到顶：子类 → 父类 → 祖先类
同层从左到右：按继承声明的顺序
每个类只访问一次：去重
```

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

# 继承树：
#       A
#      / \
#     B   C
#      \ /
#       D

# 遍历路径：
# 第1层：D (叶节点)
# 第2层：B, C (从左到右，因为 D(B, C))
# 第3层：A (根节点)
# 结果：D → B → C → A
```

1. **从子类开始**：总是从最具体的类开始
2. **左优先**：多个父类时，左边的先访问
3. **向上爬树**：逐层向上访问祖先
4. **不重复**：每个类只出现一次

**关键**：把继承想象成一棵倒置的树，MRO就是从叶子到根的有序路径！

## 常见陷阱

### 1. 错误的继承顺序

```python
# 会失败的情况
class X: pass
class Y: pass
class A(X, Y): pass
class B(Y, X): pass  # 顺序冲突
# class C(A, B): pass  # TypeError: 无法创建一致的MRO
```

### 2. super()的正确使用

```python
# 错误：直接调用父类
class Wrong(Mixin1, Mixin2):
    def method(self):
        Mixin1.method(self)  # 破坏MRO链

# 正确：使用super()
class Right(Mixin1, Mixin2):
    def method(self):
        super().method()  # 遵循MRO
```

## 实用工具

### 查看MRO

```python
# 三种方式查看MRO
print(MyClass.mro())           # 详细信息
print(MyClass.__mro__)         # 元组形式
print([c.__name__ for c in MyClass.mro()])  # 仅类名
```

### 调试函数

```python
def show_mro(cls):
    """显示类的MRO"""
    print(f"{cls.__name__} MRO:")
    for i, c in enumerate(cls.mro()):
        print(f"  {i+1}. {c.__name__}")
```

## 总结

**MRO的本质**：为多重继承提供确定性的线性查找顺序

**核心算法**：C3线性化 = 深度优先 + 左到右 + 去重合并

**关键应用**：方法调用、属性查找、super()机制

**记忆要点**：子类→左父类→右父类→共同祖先，保证单调性和局部顺序。
