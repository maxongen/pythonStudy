import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Load data
df = pd.read_csv("customer_churn.csv")  # suppose contains features and 'churn' column

# 2. Basic cleaning
df = df.drop_duplicates()
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')  # coerce bad strings
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# 3. Define features / target
target = "churn"
X = df.drop(columns=[target])
y = df[target].map({'Yes': 1, 'No': 0})  # encode target

# 4. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# 5. Preprocessing: categorical vs numeric
categorical_cols = X.select_dtypes(include="object").columns.tolist()
numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse=False), categorical_cols),
    ]
)

# 6. Pipeline with model
pipeline = Pipeline([
    ("preproc", preprocessor),
    ("clf", RandomForestClassifier(n_estimators=100, random_state=42)),
])

# 7. Train
pipeline.fit(X_train, y_train)

# 8. Predict & evaluate
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
