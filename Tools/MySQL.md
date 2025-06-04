# MySQL

MySQL是一个开源的关系型数据库管理系统(RDBMS)，使用SQL语言进行数据库操作。它以速度快、可靠性高和易用性著称，广泛应用于网站和应用程序的数据存储。

---

## 进入 MySQL

```bash
mysql -u root -p
Enter password: 
```

---

## 数据库管理

```sql
SHOW DATABASES;  -- 查看所有数据库
CREATE DATABASE mydb;  -- 创建数据库
USE mydb;  -- 使用数据库
DROP DATABASE mydb;  -- 删除数据库
```

---

## 表操作

```sql
-- 创建表
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department VARCHAR(100),
    salary DECIMAL(10,2),
    hire_date DATE,
    active BOOLEAN DEFAULT true
);

-- 查看表
SHOW TABLES;  -- 显示所有表
DESCRIBE employees;  -- 查看表结构
SHOW COLUMNS FROM employees;  -- 查看表结构

-- 修改表
ALTER TABLE employees ADD phone VARCHAR(20);  -- 添加列
ALTER TABLE employees MODIFY phone VARCHAR(15);  -- 修改列
ALTER TABLE employees DROP COLUMN phone;  -- 删除列
RENAME TABLE employees TO staff;  -- 重命名表

-- 删除表
DROP TABLE employees;
```

---

## 数据操作

```sql
-- 插入数据
INSERT INTO employees (name, email, department, salary, hire_date)
VALUES ('John Doe', 'john@example.com', 'IT', 75000.00, '2022-01-15');

INSERT INTO employees (name, email, department, salary, hire_date) VALUES    -- 插入多行
('Jane Smith', 'jane@example.com', 'HR', 65000.00, '2022-02-20'),
('Mike Johnson', 'mike@example.com', 'Sales', 80000.00, '2022-03-10');

-- 查询数据
SELECT * FROM employees;  -- 查询所有行和列
SELECT name, email, department FROM employees;  -- 查询特定列
SELECT * FROM employees WHERE department = 'IT';  -- 条件查询
SELECT * FROM employees ORDER BY salary DESC;  -- 排序
SELECT * FROM employees LIMIT 5;  -- 限制结果数量
SELECT * FROM employees LIMIT 5 OFFSET 10;  -- 分页查询（第3页，每页5条）

-- 更新数据
UPDATE employees    -- 更新单个记录 
SET salary = 78000.00 
WHERE id = 1;

UPDATE employees    -- 更新多个记录
SET active = false 
WHERE department = 'Sales';

UPDATE employees    -- 更新多个字段
SET salary = salary * 1.05, department = 'Engineering' 
WHERE department = 'IT';

-- 删除数据
DELETE FROM employees WHERE id = 3;  -- 删除特定记录
DELETE FROM employees WHERE department = 'Sales' AND active = false;  -- 条件删除
TRUNCATE TABLE employees;  -- 清空表（保留表结构）
```

---

## 高级查询

```sql
-- 比较运算符
SELECT * FROM employees WHERE salary > 70000;
SELECT * FROM employees WHERE department != 'HR';

-- 范围查询
SELECT * FROM employees WHERE salary BETWEEN 60000 AND 80000;

-- 列表匹配
SELECT * FROM employees WHERE department IN ('IT', 'Engineering');

-- 模式匹配
SELECT * FROM employees WHERE name LIKE 'J%';  -- 以J开头
SELECT * FROM employees WHERE email LIKE '%@gmail.com';  -- 以@gmail.com结尾

-- NULL值检查
SELECT * FROM employees WHERE department IS NULL;
SELECT * FROM employees WHERE department IS NOT NULL;

-- 逻辑操作符
SELECT * FROM employees WHERE department = 'IT' AND salary > 70000;
SELECT * FROM employees WHERE department = 'HR' OR department = 'Sales';
```
