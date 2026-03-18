# 导入必要的库
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 加载鸢尾花数据集
iris = load_iris()
X = iris.data  # 特征矩阵 (150个样本 x 4个特征)
y = iris.target  # 目标向量 (0:山鸢尾, 1:变色鸢尾, 2:维吉尼亚鸢尾)
feature_names = iris.feature_names
class_names = iris.target_names

# 划分训练集和测试集 (80%训练, 20%测试)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, )

# 创建决策树分类器
# 参数说明：
# criterion='entropy' - 使用信息增益作为分裂标准
# max_depth=3 - 限制树的最大深度
clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
# 训练模型
clf.fit(X_train, y_train)
# 在测试集上进行预测
y_pred = clf.predict(X_test)
# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"测试集准确率: {accuracy:.2f}")
# 可视化决策树
plt.figure(figsize=(15, 9))
plot_tree(clf, 
          feature_names=feature_names, 
          class_names=class_names,
          filled=True, 
          rounded=True)
plt.title("鸢尾花分类决策树")
plt.show()