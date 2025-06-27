# **双端队列 (deque)** 是一种可以在两端快速插入和删除的容器

```cpp
#include <iostream>
#include <deque>
using namespace std;

int main()
{
    deque<int> dq = {1, 2, 3};  // 创建双端队列
    dq.push_back(4);  // 尾部添加
    dq.push_front(0);  // 头部添加
    dq.pop_back();  // 尾部删除
    dq.pop_front();  // 头部删除

    // 支持随机访问
    dq[1] = 5;  // 修改第二个元素

    return 0;
}
```
