# 001_Python 学习项目

这是一个面向初学者的 Python 学习仓库。  
项目按“编号文件夹”组织，每个文件夹对应一个学习阶段，里面放可直接运行的小程序和注释说明。

---

## 项目目标

- 从 0 开始掌握 Python 基础语法
- 每个知识点都用一个最小可运行示例练习
- 保留学习过程记录（包括环境问题、排查过程、提交记录）

---

## 目录结构

```text
007_medical/
├─ 0000_上传git/            # Git / PyCharm / Cursor 上传记录
├─ 0001_HelloWorld/         # Hello World 入门
├─ 0002_你好世界/            # 中文版入门与运行问题记录
├─ 0003_基础语法/            # Python 关键语法小程序集合
└─ README.md                # 项目总说明（本文件）
```

---

## 环境要求

- Windows 10+
- Python 3.13（建议）
- Git
- PyCharm 或 Cursor

---

## 快速开始

### 1) 进入项目目录

```powershell
cd <你的项目目录>
# 例如：cd D:\projects\001_Python
```

### 2) 创建并激活虚拟环境（首次）

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) 运行任意示例

```powershell
python "<语法目录>\0003_if.py"
python "<语法目录>\0003_for.py"
python "<语法目录>\0003_class.py"
# 例如：python "0003_基础语法\0003_if.py"
```

---

## 0003_基础语法 学习清单（已覆盖）

- 条件与逻辑：`if` / `elif` / `else` / `and` / `or` / `not` / `in` / `is`
- 循环控制：`for` / `while` / `break` / `continue` / `pass`
- 函数相关：`def` / `return` / `lambda` / `yield` / `global`
- 模块相关：`import` / `from`
- 异常相关：`try` / `except` / `finally` / `raise` / `assert`
- 其他常用：`print` / `with` / `del` / `class` / `exec`

---

## 学习建议（初学者）

1. 每次只学 1 个文件，先运行再看注释。
2. 每学完一个关键词，自己改 1~2 行代码再运行。
3. 出现报错先看报错最后一行，再看对应文件注释。
4. 不追求一次记住，重点是“看懂 + 能跑 + 会改”。

---

## 提交流程（当前约定）

1. 写完或改完代码后先运行一次确认无误。
2. 提交信息尽量使用中文并简短明确。
3. 需要时再推送到远程仓库。

常用命令：

```powershell
git add .
git commit -m "新增某某示例"
git push
```

---

## 说明

- 本项目是学习仓库，代码以“易懂”为优先，不追求复杂封装。
- 后续会继续新增 `0004_xxx`、`0005_xxx` 等阶段目录。
