from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Dummy dataset for training the risk model
# Features: [IP_changes, Tor_usage (1=True, 0=False)]
# Labels: [0=Low risk, 1=Medium risk, 2=High risk]
X_train = np.array([[0, 0], [5, 1], [10, 1], [3, 0], [15, 1]])
y_train = np.array([0, 1, 2, 0, 2])

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

def risk_assessment(user_data):
    features = np.array([[user_data['ip_changes'], 1 if user_data['tor_usage'] else 0]])
    prediction = model.predict(features)
    risk_level = {0: 'Low', 1: 'Medium', 2: 'High'}
    return risk_level[prediction[0]]
