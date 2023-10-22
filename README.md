# Face Recognation 

This project that utlized 
1.data augmentation on images using various techniques from libraries such as PIL, scikit-image, OpenCV, TensorFlow, and Matplotlib.
2.facial embeddings from images using the InsightFace library and organizes them into labeled folders. The embeddings are then saved to a pickle file.
3. a Random Forest classifier using embeddings extracted from images. The embeddings are loaded from a pickle file, and the trained model is saved for later use.
4.Perform the script Automation
## Requirements

Before running the script, make sure you have the following requirements installed:

- Python==3.9.6
- pip install onnxruntime
- pip install pillow
- pip install scikit-image
- pip install opencv-python
- pip install tensorflow
- pip install numpy
- pip install matplotlib
- pip install imutils
- pip install insightface
- pip install onnxruntime

## Configuration

- Create a `config.ini` file with the following structure:

[Paths]
model_file = models/ovr_svm.pickle
Dataset=Dataset
dataset_folder =DA_Output/Dataset_Train
output_folder = processed_images
output_directory = empickle

[Training]
model_file = train_model/50omage_RF_FR_29_9_2023_model.pickle




##Usage

Ensure that you have the required libraries installed and the config.ini file is properly configured.


Run the script using the following command:


python main.py

The script performs the following tasks:

Executes the augmentation script as a subprocess.
Checks if the augmentation script ran successfully.
If successful, runs the embedding script as a subprocess.
Checks if the embedding script ran successfully.
If successful, proceeds with training.
Checks if the embedding file exists and then runs the training script as a subprocess.
Checks if the training script ran successfully.
Captures and displays the model's accuracy.
Checks for the existence of a confusion matrix CSV file and displays it if found.
Reads and displays the classification report from the file.
The script also records the execution time for the entire process and displays it at the end.


##Output:
Augmentaion Script:
-Augmented images are saved in an output folder, preserving the original folder structure.
-Augmented images may have filenames reflecting the applied augmentation techniques for easy reference.

Emebedding Script:
-Extracted facial embeddings are saved in a pickle file with a timestamped filename in the specified output directory.
-Processed images are organized into subfolders within the output folder, corresponding to their labels.

trainning Script :

-The trained Random Forest model is saved to the specified model file.
-The confusion matrix is saved to a CSV file named confusion_matrix.csv.
-The classification report is saved to a text file named classification_report.txt.

Main.script:
-If each step (augmentation, embedding, and training) is successful, you will see the model's accuracy, confusion matrix, and classification report.
-If any step encounters an error, it will be displayed in the console.
