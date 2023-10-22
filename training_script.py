import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
import configparser
from datetime import datetime
import pandas as pd

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Define the model file path from the configuration
model_file = config['Training']['model_file']

# Generate the embedding file path based on the current date and time
timestamp = datetime.now().strftime("%Y-%m-%d")
embedding_file = os.path.join("empickle", f"embedding_person_{timestamp}.pickle")

def train(model_file, emb_file):
    # Load the embeddings and labels from the pickle file
    with open(emb_file, 'rb') as emb_handle:
        embeddings_dict = pickle.load(emb_handle)

    # Create lists to store embeddings and labels
    X = []
    y = []

    for image_path, data in embeddings_dict.items():
        embedding = data['embedding']
        label = data['label']

        X.append(embedding)
        y.append(label)

    X = np.array(X)
    y = np.array(y)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create and train the Random Forest classifier
    random_forest = RandomForestClassifier(n_estimators=101, random_state=42)
    random_forest.fit(X_train, y_train)

    # Test the accuracy
    y_pred = random_forest.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Calculate the confusion matrix with labels
    labels = np.unique(y)
    cm = confusion_matrix(y_test, y_pred, labels=labels)

    # Display the confusion matrix with labels using pandas
    cm_df = pd.DataFrame(cm, index=labels, columns=labels)
    print("Confusion Matrix (with labels):\n", cm_df)

    # Save the confusion matrix to a file
    cm_df.to_csv("confusion_matrix.csv")

    # Calculate and print the classification report with labels
    classification_report_str = classification_report(y_test, y_pred, target_names=[f"Label {label}" for label in labels])
    print("Classification Report (with labels):\n", classification_report_str)

    # Save the classification report to a text file
    with open("classification_report.txt", "w") as report_file:
        report_file.write(classification_report_str)
    print("Classification Report saved to classification_report.txt")

    # Save the trained Random Forest model to a file
    with open(model_file, 'wb') as handle:
        pickle.dump(random_forest, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"Trained Random Forest model saved to {model_file}")

# Call the train function
train(model_file, embedding_file)
