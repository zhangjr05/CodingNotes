# string

```cpp
#include <string>
#include <iostream>
using namespace std;

int main()
{
    string s1 = "Hello";
    string s2 = "World";
    string s3 = s1 + " " + s2;
    
    // 查找和替换
    size_t pos = s3.find("World");
    s3.replace(pos, 5, "C++");

    return 0;
}
```
