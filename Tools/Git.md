# Git

Git 是一个分布式版本控制系统，用于跟踪文件的变化，协调多人协作开发。不同于集中式版本控制系统，Git 允许每个开发者在本地拥有完整的代码仓库。

---

## 创建仓库

```bash
mkdir my-project
cd my-project
git init  # 初始化仓库

git clone https://github.com/username/repository.git  # 克隆现有仓库
git clone https://github.com/username/repository.git my_project  # 自定义目录名
```

---

## 基本工作流程

```bash
git status  # 查看状态
git add file.txt  # 添加文件到暂存区
git add .  # 添加所有修改
git add *.py  # 添加所有 Python 文件

git commit -m "提交说明"
git commit -am "提交说明"  # 合并 add 和 commit 操作
git commit --amend -m "新的提交信息"  # 修改最后一次提交

git log  # 查看提交历史
git log --oneline  # 简洁日志
git log --graph --oneline  # 图形化显示

git restore file.txt  # 撤销工作区修改
git restore --staged file.txt  # 撤销暂存区修改
```

---

## 分支操作

```bash
git branch  # 查看本地分支
git branch -r  # 查看远程分支
git branch -a  # 查看所有分支

git branch feature  # 创建新分支
git checkout -b feature  # 创建并切换到新分支
git switch -c feature  # 新语法

git checkout feature  # 切换分支
git switch feature  # 新语法

git branch -d feature  # 删除分支(安全)
git branch -D feature  # 强制删除

git checkout master
git merge feature  # 将 feature 合并到当前 master 分支

# 合并发生冲突
# 手动解决冲突后
git add .
git commit
```

---

## 远程仓库操作

```bash
git remote add origin git@github.com:username/repository.git  # 使用 SSH 添加远程仓库
git remote -v  # 查看远程仓库

git push origin master  # 推送到远程仓库指定分支
git push -u origin master  # 设置上游分支并推送
git push  # 设置上游分支后可省略分支

git fetch origin  # 获取远程更新但不合并
git pull origin master  # 拉取并合并(fetch + merge)

git push origin --delete feature  # 删除远程分支
```

---

## 回退操作

```bash
# git reset
# 回退到指定提交，但保留修改在工作区 (soft)
git reset --soft HEAD~1       # 回退一个版本
git reset --soft commit_hash  # 回退到指定提交
# 回退到指定提交，并清除暂存区，保留工作区修改 (mixed，默认)
git reset HEAD~2              # 回退两个版本
git reset commit_hash         
# 回退到指定提交，并清除工作区所有修改 (hard，谨慎使用!)
git reset --hard HEAD~3       # 回退三个版本
git reset --hard commit_hash

# 使用提交 ID 回退
# 首先查看提交历史获取 commit_hash
git log --oneline
# 回退到指定提交
git reset --hard abc1234

# 撤销已推送的提交
# 使用 git revert
# 创建新提交来撤销某次提交的修改 (不改变历史)
git revert commit_hash
# 撤销多个连续提交
git revert HEAD~3..HEAD      # 撤销最近三次提交
# 只生成撤销补丁但不自动提交
git revert -n commit_hash

# 回到未来
# 查看所有操作历史 (包括已回退的提交)
git reflog
# 回到某个操作点
git reset --hard HEAD@{2}    # 回到第 2 个操作点
git checkout commit_hash     # 查看特定提交但不切换分支
```
