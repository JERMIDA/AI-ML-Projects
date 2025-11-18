import numpy as np  
from sklearn.linear_model   import LinearRegression

# step 1-Create synthetic data //datasets
# x-study hours
# y-scores

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) 
y = np.array([55, 60, 65, 70, 75])

model = LinearRegression() # think of it like a student before studying

model.fit(X, y) # look at x and y and figures out the best equation

study_hours = 6
predicted_score = model.predict([[study_hours]])
print("Predicted score:", predicted_score[0])

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)


















  








 
 















