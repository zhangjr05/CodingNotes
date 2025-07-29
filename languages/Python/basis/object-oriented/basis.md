# 类与对象

```python
# 定义一个简单的类
class Dog:
    # 类属性
    species = "Canis familiaris"
    __slots__ = ('name','age')  # 禁止动态添加其他属性

    # 初始化/实例化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def description(self):
        return f"{self.name} is {self.age} years old"

    # 另一个实例方法
    def speak(self, sound):
        return f"{self.name} says {sound}"

# 创建对象
my_dog = Dog("Buddy", 3)

# 访问类属性
print(Dog.species)

# 访问实例属性
print(my_dog.name)
print(my_dog.age)

# 调用实例方法
print(my_dog.description())
print(my_dog.speak("Woof Woof"))
```
