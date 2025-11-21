# Plotting Linear Regression Line

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1 — Dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([55, 60, 65, 70, 75])

# Step 2 — Train mode
model = LinearRegression()
model.fit(X, y)

# Step 3 — Predictions for plotting
y_pred = model.predict(X)

# Step 4 — Plotting

plt.scatter(X, y, label="Original Data")  # blue dots
plt.plot(X, y_pred, label="Best Fit Line")  # blue line

plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Linear Regression — Line of Best Fit")
plt.legend() #associates plot elements with labels

plt.show()
