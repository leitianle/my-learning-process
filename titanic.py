import pandas as pd
filepath = "C:/Users/admin/Desktop/train.csv"
df = pd.read_csv(filepath)
df["Age"]=df["Age"].fillna(df["Age"].median())
d={"male":1,"female":0}
df["Sex"]=df["Sex"].map(d)
b={"S":1,"C":2,"Q":3}
df["Embarked"]=df["Embarked"].map(b)
#df["Cabin"]=df["Cabin"].fillna(0)#预处理
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
mymodel=RandomForestClassifier(random_state=2,n_estimators=500)
features = ['Pclass', 'Sex', 'Age', 'Embarked', 'SibSp', 'Parch', 'Fare']
k = df[features]
X=k.values
y =df["Survived"]
X_train , X_test ,y_train,y_test = train_test_split(X,y,test_size=0.2)
mymodel.fit(X_train,y_train)
y_pred=mymodel.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)#模型搭完了
filepath="C:/Users/TIANLE/Desktop/test.csv"
df=pd.read_csv(filepath)
df["Age"]=df["Age"].fillna(df["Age"].median())
d={"male":1,"female":0}
df["Sex"]=df["Sex"].map(d)
b={"S":1,"C":2,"Q":3}
df["Embarked"]=df["Embarked"].map(b)
kk=df[features]
XX=kk.values
suvived=mymodel.predict(XX)
df["Survived"] = suvived

# 选择需要保存的列（通常只需要乘客ID和预测结果）
# 如果您想保存所有列加上预测结果，可以直接保存整个DataFrame
result_df = df[["PassengerId", "Survived"]]

# 保存到CSV文件
output_path = "C:/Users/admin/Desktop/test_predictions.csv"
result_df.to_csv(output_path, index=False)

print(f"预测结果已保存到: {output_path}")
print(f"共预测了 {len(suvived)} 名乘客的生存情况")



