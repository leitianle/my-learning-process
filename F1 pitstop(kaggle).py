import pandas as pd
import numpy as np
import xgboost as xgb
import optuna
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
sample_sub = pd.read_csv('sample_submission.csv')

# 2. 深度特征工程 (Feature Engineering)
def create_features(df):
    df = df.copy()
    
    # 轮胎寿命占当前航段的比例
    df['TyreLife_Progress'] = df['TyreLife'] / (df['LapNumber'] + 1)
    
    # 单圈时间与累积退化的交互
    df['Degradation_Rate'] = df['Cumulative_Degradation'] / (df['TyreLife'] + 1)
    
    # C. 策略特征：计算该车手在当前分站的历史平均表现
    df['Race_Lap_Ratio'] = df['LapNumber'] / (df['RaceProgress'] + 1e-5)
    
    # 类别特征转换
    cat_cols = ['Driver', 'Compound', 'Race']
    for col in cat_cols:
        df[col] = df[col].astype('category')
        
    return df

train_df = create_features(train)
test_df = create_features(test)

X = train_df.drop(['id', 'PitNextLap'], axis=1)
y = train_df['PitNextLap']
X_test = test_df.drop(['id'], axis=1)

# 3. 使用 Optuna 寻找最优超参数
def objective(trial):
    param = {
        'n_estimators': 1000,
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.1),
        'subsample': trial.suggest_float('subsample', 0.6, 0.9),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 0.9),
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
        'enable_categorical': True,
        'tree_method': 'hist',
        'eval_metric': 'auc',
        'random_state': 42
    }
    
    x_t, x_v, y_t, y_v = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    model = xgb.XGBClassifier(**param, early_stopping_rounds=50)
    model.fit(x_t, y_t, eval_set=[(x_v, y_v)], verbose=False)
    
    return roc_auc_score(y_v, model.predict_proba(x_v)[:, 1])

# study = optuna.create_study(direction='maximize')
# study.optimize(objective, n_trials=50)
# best_params = study.best_params


best_params = {
    'n_estimators': 2000,
    'max_depth': 6,
    'learning_rate': 0.02,
    'subsample': 0.85,
    'colsample_bytree': 0.75,
    'min_child_weight': 4,
    'enable_categorical': True,
    'tree_method': 'hist',
    'eval_metric': 'auc',
    'random_state': 42
}

# 4. 5 折交叉验证训练 (K-Fold Ensemble)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
oof_preds = np.zeros(len(X))
test_preds = np.zeros(len(X_test))

print("开始 5 折交叉验证训练...")
for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
    X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]
    
    model = xgb.XGBClassifier(**best_params, early_stopping_rounds=100)
    model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=200)
    
    oof_preds[val_idx] = model.predict_proba(X_val)[:, 1]
    test_preds += model.predict_proba(X_test)[:, 1] / 5
    
    print(f"Fold {fold+1} AUC: {roc_auc_score(y_val, oof_preds[val_idx]):.4f}")

print(f"\n整体 OOF AUC: {roc_auc_score(y, oof_preds):.4f}")

# 5. 生成提交文件
sample_sub['PitNextLap'] = test_preds # 这里提交的是概率，很多比赛概率分更高，如果必须是0/1则加 .round()
sample_sub.to_csv('submission_optimized.csv', index=False)
print("优化后的提交文件已生成！")



