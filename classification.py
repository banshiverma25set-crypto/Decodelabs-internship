from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# ==========================================
# IRIS FLOWER CLASSIFICATION PROJECT
# ==========================================

print("=" * 60)
print("        IRIS FLOWER CLASSIFICATION SYSTEM")
print("=" * 60)

# Load the dataset
iris = load_iris()

X = iris.data
y = iris.target

# Display dataset information
print("\nDataset Information")
print("----------------------------")
print("Total Samples :", len(X))
print("Number of Features :", len(iris.feature_names))
print("Feature Names :", iris.feature_names)
print("Flower Classes :", iris.target_names)

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create the Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Trained Successfully!")
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print classification report
print("\nClassification Report")
print("----------------------------")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))

# Sample predictions
print("\nSample Predictions")
print("----------------------------")

sample_flowers = [
    [5.1, 3.5, 1.4, 0.2],
    [6.0, 2.9, 4.5, 1.5],
    [6.9, 3.1, 5.4, 2.1]
]

for sample in sample_flowers:
    result = model.predict([sample])
    flower = iris.target_names[result[0]]
    print(f"{sample} --> {flower}")

# ------------------------------------------
# Custom Prediction by User
# ------------------------------------------

print("\nTry Your Own Prediction")
print("----------------------------")

choice = input("Do you want to enter your own values? (yes/no): ").lower()

if choice == "yes":
    try:
        sepal_length = float(input("Enter Sepal Length (cm): "))
        sepal_width = float(input("Enter Sepal Width (cm): "))
        petal_length = float(input("Enter Petal Length (cm): "))
        petal_width = float(input("Enter Petal Width (cm): "))

        user_data = [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]]

        prediction = model.predict(user_data)

        print("\nPrediction Result")
        print("----------------------------")
        print("Predicted Flower:",
              iris.target_names[prediction[0]])

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

else:
    print("Custom prediction skipped.")

print("\nThank you for using the Iris Flower Classification System!")