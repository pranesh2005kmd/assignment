from flask import Flask, jsonify
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create a RandomForest Classifier
clf = RandomForestClassifier()

# Train the model using the training sets
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Save the trained model
joblib.dump(clf, 'iris_model.pkl')
print("Model saved!")

# Flask API for Prediction
app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    sample_input = X_test[0].reshape(1, -1)  # Take one sample for testing
    model = joblib.load('iris_model.pkl')
    prediction = model.predict(sample_input)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)  # Running on port 6000
