<div align="center">

# my-learning-process

**在代码中理解统计，在数据中验证想法。**

一份持续更新的学习档案：从 C 语言、算法与数据结构，到 Python 数据分析、统计建模、机器学习与 Kaggle 实践。

<br>

![Status](https://img.shields.io/badge/Status-Learning%20in%20Progress-2ea44f?style=for-the-badge)
![Code](https://img.shields.io/badge/Code-C%20%7C%20Python-2563eb?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Data%20Science-f59e0b?style=for-the-badge)
![Practice](https://img.shields.io/badge/Practice-Kaggle-0f766e?style=for-the-badge)

</div>

---

## 关于仓库

`my-learning-process` 是我的个人学习仓库，用来沉淀课程练习、编程实验和数据分析项目。

这里记录的不只是最终代码，也包括从基础语法、算法实现到数据预处理、模型训练和结果生成的完整探索过程。

目前仓库包含 **6 个 C 语言练习、5 个 Python 项目，以及 4 份课程作业**，内容覆盖：

- C 语言与程序设计基础
- 算法、数值方法与数据结构
- Python 数据分析
- 机器学习与深度学习
- Kaggle 数据建模实践
- 统计学专业课程作业

---

## 内容导航

### C 语言与算法

| 文件 | 练习内容 |
| --- | --- |
| [`4int to 24.c`](./4int%20to%2024.c) | 使用四个整数组成 24 点 |
| [`Newton method.c`](./Newton%20method.c) | 牛顿迭代法求解方程 |
| [`find min n.c`](./find%20min%20n.c) | 求 n 个数中的最小值 |
| [`solve an equation.C`](./solve%20an%20equation.C) | 方程求解练习 |
| [`using GCD2output LCM.c`](./using%20GCD2output%20LCM.c) | 通过最大公约数计算最小公倍数 |
| [`shunxubiao.c`](./shunxubiao.c) | 顺序表与基础数据结构操作 |

### Python 与机器学习

| 文件 | 数据任务 | 使用的方法 |
| --- | --- | --- |
| [`titanic.py`](./titanic.py) | Titanic 乘客生存预测 | 缺失值处理、类别编码、随机森林 |
| [`F1 pitstop(kaggle).py`](./F1%20pitstop(kaggle).py) | F1 进站预测 | 特征工程、XGBoost、Optuna、5 折交叉验证 |
| [`MINST.py`](./MINST.py) | MNIST 手写数字识别 | PyTorch、CNN、GPU/CPU 自动切换 |
| [`房价预测.py`](./房价预测.py) | 房屋价格回归预测 | 数据清洗、LabelEncoder、随机森林回归 |
| [`鸢尾花分类决策树.py`](./鸢尾花分类决策树.py) | Iris 鸢尾花分类 | 决策树、信息熵、模型可视化 |

仓库根目录同时保存了四份课程作业 PDF，作为学习过程的一部分。

---

## 技术栈

**编程语言**

- C
- Python

**Python 生态**

- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- PyTorch
- XGBoost
- Optuna

**学习方向**

- Programming Fundamentals
- Algorithms and Data Structures
- Numerical Methods
- Statistics
- Data Analysis
- Machine Learning
- Kaggle Practice

---

## 快速开始

克隆仓库并进入项目目录：

```powershell
git clone https://github.com/leitianle/my-learning-process.git
cd my-learning-process
```

建议为 Python 项目创建独立虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

安装常用依赖：

```powershell
python -m pip install numpy pandas matplotlib scikit-learn xgboost optuna
```

运行 PyTorch 项目前，再根据自己的操作系统和 GPU 环境安装 PyTorch：

```powershell
python -m pip install torch torchvision
```

运行示例：

```powershell
python "鸢尾花分类决策树.py"
python "MINST.py"
```

编译一个 C 程序：

```powershell
gcc "Newton method.c" -o newton
.\newton.exe
```

---

## 数据与运行说明

- `titanic.py`、`F1 pitstop(kaggle).py` 和 `房价预测.py` 需要对应的 CSV 数据集，部分数据文件未包含在仓库中。
- 部分脚本仍保留本机绝对路径，运行前需要将数据路径修改为自己的路径。
- `MINST.py` 会通过 `torchvision` 自动下载 MNIST 数据集。
- `鸢尾花分类决策树.py` 使用 Scikit-learn 内置的 Iris 数据集，可以直接运行。
- 当前项目以学习记录为主，因此暂未统一依赖版本和实验配置。

---

## 学习路线

<div align="center">

**C 语言基础**  
↓  
**算法、数值方法与数据结构**  
↓  
**Python 数据分析**  
↓  
**统计建模**  
↓  
**机器学习与深度学习**  
↓  
**Kaggle 项目实践**

</div>

---

## 当前重点

- 从基础语法逐步走向完整的数据建模流程
- 同时练习底层编程能力与 Python 数据科学工具
- 通过 Kaggle 项目理解特征工程、交叉验证和模型评估
- 将统计思维应用到真实数据与机器学习任务中
- 保持代码、实验和课程成果的长期积累

---

## 下一步计划

- 将根目录文件整理到 `c/`、`python/`、`machine-learning/` 和 `coursework/`
- 为每个重点项目增加独立说明、运行方式和实验结果
- 移除代码中的本机绝对路径，改为统一的数据路径配置
- 添加 `requirements.txt`，提高项目复现性
- 为 Kaggle 项目补充评价指标、模型对比和结论
- 继续加入新的统计建模与数据科学实践

---

## About Me

我是一名统计学专业学生，正在持续学习编程、统计建模、数据分析与机器学习。

这个仓库记录我从课堂练习走向真实数据项目的轨迹。代码会继续更新，方法也会不断调整，希望每一次提交都能留下清晰可见的进步。

<div align="center">

**Learning by doing. Growing through data and code.**

</div>
