# json

```python
import json

data = {
    'name': '张三',
    'age': '20',
    'skills': ['python', 'c/c++', 'algorithms'],
    'is_active': True,
    'university': 'NJU',
    'major': 'AI',
    'address': {
        'city': '南京',
        'district': '鼓楼区',
    }
}

data_json = json.dumps(data, ensure_ascii=False, indent=4)


with open('demo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

with open('demo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```
