import os
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import graphviz
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

wine = load_wine()
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 100)
result = pd.concat(
    [pd.DataFrame(wine.data), pd.DataFrame(wine.target)], axis=1)
print(result)

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(
    wine.data, wine.target, test_size=0.2, random_state=42)

# 创建可配置的决策树分类器
clf = tree.DecisionTreeClassifier(
    max_depth=3,                # 控制树的最大深度
    min_samples_split=2,       # 节点最少样本数才能继续分裂
    criterion="gini",          # 分裂标准（gini/entropy）
    random_state=42,           # 随机种子保证可重复性
    min_impurity_decrease=0.01  # 最小不纯度减少阈值
)

# 训练模型
clf.fit(X_train, y_train)

# 评估模型
score = clf.score(X_test, y_test)
print(f"测试集准确率：{score:.2%}")

# 预测测试集
y_pred = clf.predict(X_test)
print("\n分类报告：")
print(classification_report(y_test, y_pred))

# 可视化决策树
# 可视化决策树（添加更多配置）
plt.figure(figsize=(18, 8), dpi=300)
tree.plot_tree(clf,
               feature_names=wine.feature_names,
               class_names=wine.target_names.astype(str),
               filled=True,
               proportion=True,
               fontsize=8,
               node_ids=True)
plt.title("葡萄酒分类决策树结构", fontsize=14)
# 使用graphviz生成更清晰的树结构
dot_data = tree.export_graphviz(clf,
                                out_file=None,
                                feature_names=wine.feature_names,
                                class_names=wine.target_names.astype(str),
                                filled=True,
                                rounded=True)
graph = graphviz.Source(dot_data)
# 确保Graphviz路径正确
graphviz_path = 'C:/Program Files/Graphviz/bin'
if os.path.exists(graphviz_path):
    os.environ["PATH"] += os.pathsep + graphviz_path

try:
    # 使用英文路径避免编码问题
    output_path = os.path.join(os.getcwd(), "wine_tree")
    graph.render(output_path, encoding='gbk')  # 生成PDF和DOT文件
    print(f"决策树已成功保存到: {output_path}")
except Exception as e:
    print(f"生成决策树时出错: {str(e)}")
    print("请检查Graphviz是否正确安装并添加到系统PATH")

# 显示特征重要性
# 可视化特征重要性（排序后）
sorted_idx = clf.feature_importances_.argsort()
plt.figure(figsize=(12, 6))
plt.barh(np.array(wine.feature_names)[sorted_idx],
         clf.feature_importances_[sorted_idx],
         color=plt.cm.viridis(clf.feature_importances_[sorted_idx]))
plt.xlabel('重要性分数', fontsize=12)
plt.ylabel('特征名称', fontsize=12)
plt.title('葡萄酒数据集特征重要性排序', fontsize=14)
plt.grid(axis='x', alpha=0.5)
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.show()

# 输出混淆矩阵
print("\n混淆矩阵：")
print(confusion_matrix(y_test, y_pred))

# 输出测试集样本预测示例
print("\n测试集前5个样本的预测结果：")
for i in range(5):
    print(f"样本{i+1}: 真实类别={y_test[i]}, 预测类别={y_pred[i]}")
