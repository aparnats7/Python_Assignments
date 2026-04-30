import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

print("Step 1: Creating dataset\n")

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])

y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])

print("Step 2: Scaling data\n")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Step 3: Training model\n")

model = MLPClassifier(hidden_layer_sizes=(5, 3), max_iter=500, random_state=42)
model.fit(X_scaled, y)

print("Step 4: Evaluating model\n")

y_pred = model.predict(X_scaled)
print("Accuracy:", accuracy_score(y, y_pred))

print("Step 5: Testing new applicant\n")

new_applicant = np.array([[55000, 720, 400000, 10000, 1]])
new_scaled = scaler.transform(new_applicant)

prediction = model.predict(new_scaled)

if prediction[0] == 1:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")