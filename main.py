import subprocess
import time
import os
from datetime import datetime
import numpy as np
import pandas as pd  # Import pandas library

# Define the paths to your Python scripts for embedding and training
augmentation_script = "Da_main.py" # Add the path to your augmentation script
embedding_script = "embedding_script.py"
training_script = "training_script.py"

# Record the start time
start_time = time.time()

# Run the augmentation script as a subprocess
augmentation_process = subprocess.Popen(["python", augmentation_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
augmentation_stdout, augmentation_stderr = augmentation_process.communicate()

# Check if the augmentation script ran successfully
if augmentation_process.returncode == 0:
    print("Augmentation script ran successfully.")
    
    # Run the embedding script as a subprocess
    embedding_process = subprocess.Popen(["python", embedding_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    embedding_stdout, embedding_stderr = embedding_process.communicate()

    # Check if the embedding script ran successfully
    if embedding_process.returncode == 0:
        print("Embedding script ran successfully.")
        
        # Generate a timestamp for the expected embedding file name
        timestamp = datetime.now().strftime("%Y-%m-%d")
        embedding_file = f"empickle/embedding_person_{timestamp}.pickle"

        # Check if the embedding file exists
        if os.path.exists(embedding_file):
            print(f"Embedding file '{embedding_file}' exists. Proceeding with training...")

            # Run the training script as a subprocess
            training_process = subprocess.Popen(["python", training_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            training_stdout, training_stderr = training_process.communicate()

            # Check if the training script ran successfully
            if training_process.returncode == 0:
                print("Training script ran successfully.")
                
                # Capture and display the model's accuracy
                training_output = training_stdout.decode()
                accuracy_line = [line for line in training_output.split('\n') if line.startswith('Accuracy: ')]
                if accuracy_line:
                    model_accuracy = float(accuracy_line[0].split(':')[1].strip())
                    print(f"Model Accuracy: {model_accuracy:.2%}")
                else:
                    print("Model accuracy not found in training output.")
                
                # Check if the confusion_matrix.csv file exists
                confusion_matrix_csv_file = "confusion_matrix.csv"
                if os.path.exists(confusion_matrix_csv_file):
                    # Read the confusion matrix from the CSV file using pandas
                    confusion_matrix_df = pd.read_csv(confusion_matrix_csv_file, index_col=0)
                    
                    # Display the confusion matrix
                    print("Confusion Matrix:")
                    print(confusion_matrix_df)
                else:
                    print(f"Confusion matrix CSV file '{confusion_matrix_csv_file}' not found.")

                # Read and display the classification report from the file
                classification_report_file = "classification_report.txt"
                if os.path.exists(classification_report_file):
                    with open(classification_report_file, 'r') as report_file:
                        classification_report_content = report_file.read()
                        print("Classification Report:")
                        print(classification_report_content)
                else:
                    print(f"Classification report file '{classification_report_file}' not found.")
            else:
                print("Training script encountered an error.")
                print("Training script stdout:\n", training_stdout.decode())
                print("Training script stderr:\n", training_stderr.decode())
        else:
            print(f"Embedding file '{embedding_file}' does not exist. Training skipped.")
    else:
        print("Embedding script encountered an error.")
        print("Embedding script stdout:\n", embedding_stdout.decode())
        print("Embedding script stderr:\n", embedding_stderr.decode())
else:
    print("Augmentation script encountered an error.")
    print("Augmentation script stdout:\n", augmentation_stdout.decode())
    print("Augmentation script stderr:\n", augmentation_stderr.decode())

# Record the end time for the entire process
end_time = time.time()

# Calculate and print the total script execution time
total_execution_time = end_time - start_time
print(f"Total script execution time: {total_execution_time:.2f} seconds")
