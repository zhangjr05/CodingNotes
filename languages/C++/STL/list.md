# list

```cpp
#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

int main()
{
    list<int> lst = {1, 2, 3, 4, 5};  // 创建双向链表

    // 添加删除
    lst.push_back(6);
    lst.push_front(0);
    lst.pop_back();
    lst.pop_front();

    // 插入移除
    auto it = find(lst.begin(), lst.end(), 3);  // 找到链表中元素3的位置
    lst.insert(it, 2);  // 3前插入2
    lst.erase(it);  // 删除3

    // 合并拼接
    list<int> lst2 = {10, 20, 30};
    lst.splice(lst.begin(), lst2);  // 将lst2元素移到lst前端
    // lst: {10, 20, 30, 1, 2, 4, 5}, lst2: {} 为空

    lst.sort();  // 排序
    lst.unique();  // 移除连续重复元素
    lst.reverse();  // 反转链表

    return 0;
}
```
