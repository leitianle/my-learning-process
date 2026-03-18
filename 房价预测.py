import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# 1. 数据加载
filepath = "C:/Users/admin/Desktop/train.csv"
train_df = pd.read_csv(filepath)
filepath="C:/Users/TIANLE/Desktop/test.csv"
test_df=pd.read_csv(filepath)


# 2. 数据预处理
# 处理缺失值
def handle_missing_data(df):
    # 数值列用中位数填充
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)
    
    # 分类列用众数填充
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    return df

train_df = handle_missing_data(train_df)
test_df = handle_missing_data(test_df)

# 3. 特征工程
# 编码分类变量
def encode_categorical(df):
    le = LabelEncoder()
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])
    return df

train_df = encode_categorical(train_df)
test_df = encode_categorical(test_df)

# 4. 准备训练数据
X = train_df.drop(['Id', 'SalePrice'], axis=1)
y = train_df['SalePrice']

# 5. 划分训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. 训练模型
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 7. 验证模型
val_pred = model.predict(X_val)
rmse = np.sqrt(mean_squared_error(y_val, val_pred))
print(f"验证集RMSE: {rmse:.2f}")

# 8. 预测测试集
test_ids = test_df['Id']
test_features = test_df.drop('Id', axis=1)
test_pred = model.predict(test_features)

# 9. 保存结果
submission = pd.DataFrame({'Id': test_ids, 'SalePrice': test_pred})
output_path = "C:/Users/TIANLE/Desktop/test_predictions.csv"
submission.to_csv(output_path, index=False)
print("预测结果已保存到 submission.csv")
