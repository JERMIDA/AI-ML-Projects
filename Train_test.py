# Train/Test Split + Accuracy

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Step 1 — Dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # study hours
y = np.array([55, 60, 65, 70, 75])  # scores

# Step 2 — Split into train and test
# test_size=0.4 → 40% data used for testing (ensures at least 2 test samples)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

print("Training data:\n", X_train.flatten())
print("Testing data:\n", X_test.flatten())

# Step 3 — Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4 — Predict on test data
y_pred = model.predict(X_test)

print("\nPredicted:", y_pred)
print("Actual:   ", y_test)

# Step 5 — Measure accuracy (R² score) // how well the model fits the data
if len(y_test) >= 2:
    score = r2_score(y_test, y_pred)
    print("\nModel Accuracy (R² Score):", score)
else:
    print("\nNot enough test samples to compute R² Score (need at least 2).")