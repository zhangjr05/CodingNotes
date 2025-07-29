# vector

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // 创建与初始化
    vector<int> v1;  // 空向量
    vector<int> v2(5);  // 5个0
    vector<int> v3(5, 10);  // 5个10
    vector<int> v4 = {1, 2, 3, 4};  // 初始化列表

    // 常用操作
    v1.push_back(1);  // 尾部添加元素
    v1.pop_back();  // 删除最后一个元素
    v1.size();  // 获取元素个数
    v1.empty();  // 判断是否为空
    v1.clear();  // 清空所有元素
    v1.resize(10);  // 调整大小
    v1.reserve(100);  // 预留空间但不改变size
    vector<int>::iterator it = v1.begin();  // 返回首元素迭代器
    advance(it, 3);  // 将迭代器按指定偏移量移动

    // 访问元素
    int a = v1[0];  // 通过下标访问(不检查边界)
    int b = v1.at(0);  // 通过at方法(会检查边界)
    int front = v1.front();  // 第一个元素
    int back = v1.back();  // 最后一个元素

    // 插入与删除
    v1.insert(it, 10); // 通过访问迭代器得到插入位置
    v1.insert(v1.begin() + 3, 10);  // 插入
    v1.erase(v1.begin() + 3);  // 删除指定位置元素

    return 0;
}
```
