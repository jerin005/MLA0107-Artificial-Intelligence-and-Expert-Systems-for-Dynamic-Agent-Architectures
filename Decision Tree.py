from sklearn.tree import DecisionTreeClassifier

# Step 1: Training dataset
# Features: [Age, Income Level]
X = [
    [25,1],
    [30,0],
    [45,1],
    [35,0]
]

# Step 2: Target output
# Yes -> Buys Product
# No -> Does Not Buy
Y = ["Yes","No","Yes","No"]

# Step 3: Create Decision Tree Model
model = DecisionTreeClassifier()

# Step 4: Train the model
model.fit(X,Y)

# Step 5: New data for prediction
new_data = [[40,1]]

# Step 6: Predict result
prediction = model.predict(new_data)

print("Input Data (Age, Income):", new_data)
print("Prediction:", prediction)
