import os
import pickle
import cv2
from insightface.app import FaceAnalysis
import shutil
import numpy as np
from datetime import datetime
import configparser
import time


# Record the start time
start_time = time.time()
# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Load the trained SVM model
model_file = os.path.join(config['Paths']['model_file'])

# Initialize the FaceAnalysis app with adjusted face detection threshold
app = FaceAnalysis(name="buffalo_l", model_name="ArcFace_mxnet", root="./models", nms_thres=0.80)
app.prepare(ctx_id=0, det_size=(480, 480), det_thresh=0.6)  # Adjust det_thresh as needed

# Specify the path to your dataset folder
dataset_folder = os.path.join(config['Paths']['dataset_folder'])

# Specify the path to the folder where you want to move the processed images
output_folder = os.path.join(config['Paths']['output_folder'])

# Function to extract embeddings from a single image and move it to the output folder
def extract_embeddings_and_move(image_path):
    try:
        # Load and process the image
        test_image = cv2.imread(image_path)
        rgb_arr = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
        emb_res = app.get(rgb_arr)

        # Handle cases where no face or multiple faces are found
        if len(emb_res) == 0:
            print(f"No faces found in {image_path}.")
        elif len(emb_res) > 1:
            print(f"Multiple faces found in {image_path}.")
        else:
            embedding = emb_res[0].embedding
            label = os.path.basename(os.path.dirname(image_path))  # Get the label from the parent folder name

            # Move the processed image to the output folder
            label_output_folder = os.path.join(output_folder, label)
            os.makedirs(label_output_folder, exist_ok=True)
            output_path = os.path.join(label_output_folder, os.path.basename(image_path))
            shutil.move(image_path, output_path)

            return {
                'label': label,
                'embedding': embedding
            }
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")
        return None

# Dictionary to store embeddings with image file paths as keys and labels as values
embeddings_dict = {}

# Iterate through subfolders and their images
for root, dirs, files in os.walk(dataset_folder):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(root, file)
            result = extract_embeddings_and_move(image_path)
            if result is not None:
                embeddings_dict[image_path] = result

# Define the output directory
output_directory = os.path.join(config['Paths']['output_directory'])

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Get the current date and time as a timestamp
timestamp = datetime.now().strftime("%Y-%m-%d")

# Construct the output file path
output_pickle_file = os.path.join(output_directory, f"embedding_person_{timestamp}.pickle")

# Save the embeddings_dict to the output pickle file
with open(output_pickle_file, 'wb') as output_handle:
    pickle.dump(embeddings_dict, output_handle)

print(f"Embeddings dictionary saved to {output_pickle_file}")

# Record the end time
end_time = time.time()

# Calculate and print the execution time
execution_time = end_time - start_time
print(f"Embedding_Script execution time: {execution_time:.2f} seconds")
