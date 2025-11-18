#  Simple Linear Prediction

# Formula 1: y = 2x + 1

# lists
data = [0, 1, 2, 3, 4, 5]

predictions_1 = [] 
#  loop
for x in data:
    y = 2 * x + 1
    predictions_1.append(y)
    print(f"x={x}, y={y}")

print("Predictions for formula y = 2x + 1:", predictions_1)


# Formula 2: y = 3x + 2

predictions_2 = []

for x in range(11):  # x from 0 to 10
    y = 3 * x + 2
    predictions_2.append(y)

print("Predictions for formula y = 3x + 2:", predictions_2)
