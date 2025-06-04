# Apriori算法

Apriori算法是一种经典的关联规则挖掘算法，用于发现数据集中项目之间的频繁关联模式。算法基于"频繁项集的所有子集也必须是频繁的"这一先验知识（Apriori性质）。

- **支持度(Support)**: 项集在数据集中出现的频率
- **置信度(Confidence)**: 关联规则的可靠性度量  
- **频繁项集**: 支持度大于等于最小支持度阈值的项集
- **关联规则**: A → B形式的规则，表示A出现时B也倾向于出现

---

## 算法步骤

- **初始化**
  - 设定最小支持度阈值和最小置信度阈值
  - 扫描数据库，统计所有1-项集的支持度

- **生成频繁1-项集**
  - 过滤掉支持度小于阈值的1-项集
  - 得到频繁1-项集L₁

- **迭代生成频繁k-项集**

    ```text
    For k = 2, 3, 4, ... do:
        1. 候选生成：由L_{k-1}生成候选k-项集C_k
        2. 候选剪枝：利用Apriori性质删除不可能频繁的候选项
        3. 支持度计算：扫描数据库计算C_k中每个候选项的支持度
        4. 频繁项集确定：过滤得到L_k
        5. 如果L_k为空，则算法终止
    ```

- **关联规则生成**
  - 对每个频繁项集，生成所有可能的关联规则
  - 计算置信度，过滤出满足最小置信度的规则

---

## 代码实现

```python
from itertools import combinations
from collections import defaultdict

class Apriori:
    def __init__(self, min_support=0.3, min_confidence=0.6):
        self.min_support = min_support
        self.min_confidence = min_confidence
    
    def get_frequent_1_itemsets(self, transactions):
        """生成频繁1-项集"""
        item_count = defaultdict(int)
        total_transactions = len(transactions)
        
        # 统计每个项的出现次数
        for transaction in transactions:
            for item in transaction:
                item_count[item] += 1
        
        # 计算支持度并过滤
        frequent_1_itemsets = {}
        for item, count in item_count.items():
            support = count / total_transactions
            if support >= self.min_support:
                frequent_1_itemsets[frozenset([item])] = support
        
        return frequent_1_itemsets
    
    def generate_candidates(self, frequent_itemsets, k):
        """生成k-项候选集"""
        candidates = []
        itemsets = list(frequent_itemsets.keys())
        
        # 连接步骤：合并两个(k-1)-项集
        for i in range(len(itemsets)):
            for j in range(i + 1, len(itemsets)):
                union = itemsets[i] | itemsets[j]
                if len(union) == k:
                    candidates.append(union)
        
        return candidates
    
    def calculate_support(self, candidates, transactions):
        """计算候选集支持度"""
        candidate_count = defaultdict(int)
        total_transactions = len(transactions)
        
        # 统计候选集在事务中的出现次数
        for transaction in transactions:
            transaction_set = set(transaction)
            for candidate in candidates:
                if candidate.issubset(transaction_set):
                    candidate_count[candidate] += 1
        
        # 计算支持度并过滤
        frequent_itemsets = {}
        for candidate, count in candidate_count.items():
            support = count / total_transactions
            if support >= self.min_support:
                frequent_itemsets[candidate] = support
        
        return frequent_itemsets
    
    def find_frequent_itemsets(self, transactions):
        """查找所有频繁项集"""
        all_frequent_itemsets = {}
        
        # 生成频繁1-项集
        frequent_itemsets = self.get_frequent_1_itemsets(transactions)
        all_frequent_itemsets.update(frequent_itemsets)
        
        k = 2
        # 迭代生成k-项集
        while frequent_itemsets:
            candidates = self.generate_candidates(frequent_itemsets, k)
            if not candidates:
                break
            
            frequent_itemsets = self.calculate_support(candidates, transactions)
            all_frequent_itemsets.update(frequent_itemsets)
            k += 1
        
        return all_frequent_itemsets
    
    def generate_rules(self, frequent_itemsets):
        """生成关联规则"""
        rules = []
        
        for itemset, support in frequent_itemsets.items():
            if len(itemset) < 2:
                continue
            
            # 生成所有可能的前件和后件组合
            for i in range(1, len(itemset)):
                for antecedent in combinations(itemset, i):
                    antecedent = frozenset(antecedent)
                    consequent = itemset - antecedent
                    
                    # 计算置信度
                    antecedent_support = frequent_itemsets.get(antecedent, 0)
                    if antecedent_support > 0:
                        confidence = support / antecedent_support
                        if confidence >= self.min_confidence:
                            rules.append({
                                'antecedent': set(antecedent),
                                'consequent': set(consequent),
                                'support': support,
                                'confidence': confidence
                            })
        
        return rules

# 使用示例
if __name__ == "__main__":
    # 购物篮数据
    transactions = [
        ['牛奶', '面包', '黄油'],
        ['牛奶', '面包'],
        ['牛奶', '尿布', '啤酒', '鸡蛋'],
        ['面包', '尿布', '啤酒', '可乐'],
        ['牛奶', '面包', '尿布', '啤酒'],
        ['面包', '尿布', '啤酒'],
        ['面包', '尿布'],
        ['牛奶', '面包', '尿布', '可乐']
    ]
    
    # 创建Apriori实例
    apriori = Apriori(min_support=0.25, min_confidence=0.6)
    
    # 挖掘频繁项集
    frequent_itemsets = apriori.find_frequent_itemsets(transactions)
    
    print("=== 频繁项集 ===")
    for itemset, support in sorted(frequent_itemsets.items(), 
                                 key=lambda x: (len(x[0]), x[1]), reverse=True):
        print(f"{set(itemset)}: {support:.3f}")
    
    # 生成关联规则
    rules = apriori.generate_rules(frequent_itemsets)
    
    print("\n=== 关联规则 ===")
    for rule in sorted(rules, key=lambda x: x['confidence'], reverse=True):
        print(f"{rule['antecedent']} → {rule['consequent']}")
        print(f"  支持度: {rule['support']:.3f}")
        print(f"  置信度: {rule['confidence']:.3f}")
        print()
```

---

## 算法特点

- **优点**
  - 算法思想简单直观
  - 结果准确可靠
  - 适用于稀疏数据

- **缺点**
  - 需要多次扫描数据库，时间复杂度高
  - 候选集生成开销大
  - 内存消耗较大

- **应用场景**
  - **购物篮分析**: "买面包的顾客也经常买牛奶"
  - **推荐系统**: 基于关联规则的商品推荐
  - **网站分析**: 用户行为路径分析
  - **生物信息学**: 基因序列模式发现
