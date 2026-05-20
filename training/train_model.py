print("Step 1: Importing required libraries...")
import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from training.train_utils import DATA_FILE_PATH, MODEL_DIR, MODEL_PATH

print("Step 2: Loading and cleaning dataset...")
df = (
    pd
    .read_csv(DATA_FILE_PATH)
    .drop_duplicates()
    .drop(columns=['name', 'model', 'edition'])
)

print("Dataset loaded successfully")
print(f"Dataset shape: {df.shape}")

print("Step 3: Splitting features and target...")
X = df.drop(columns='selling_price')
y = df.selling_price.copy()

print("Features and target separated")

print("Step 4: Performing train-test split...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples: {X_test.shape[0]}")

print("Step 5: Identifying numerical and categorical columns...")
num_cols = X_train.select_dtypes(include='number').columns.tolist()
cat_cols = [col for col in X_train.columns if col not in num_cols]

print(f"Numerical columns: {num_cols}")
print(f"Categorical columns: {cat_cols}")

print("Step 6: Creating numerical preprocessing pipeline...")
num_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

print("Numerical pipeline created")

print("Step 7: Creating categorical preprocessing pipeline...")
cat_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

print("Categorical pipeline created")

print("Step 8: Combining preprocessing pipelines...")
preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipe, num_cols),
    ('cat', cat_pipe, cat_cols)
])

print("Preprocessor created successfully")

print("Step 9: Initializing Random Forest Regressor...")
regressor = RandomForestRegressor(
    n_estimators=10,
    max_depth=5,
    random_state=42
)

print("Random Forest model initialized")

print("Step 10: Creating final ML pipeline...")
rf_model = Pipeline(steps=[
    ('pre', preprocessor),
    ('reg', regressor)
])

print("Pipeline created successfully")

print("Step 11: Training the model...")
rf_model.fit(X_train, y_train)

print("Model training completed")

print("Step 12: Creating model directory...")
os.makedirs(MODEL_DIR, exist_ok=True)

print("Step 13: Saving trained model...")
joblib.dump(rf_model, MODEL_PATH)

print(f"Model saved successfully at: {MODEL_PATH}")

print("All steps executed successfully!")