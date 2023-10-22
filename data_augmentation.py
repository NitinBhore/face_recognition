import os
import cv2
import albumentations as A
import time  # Import the time module

def augment_images_in_subfolders(root_folder, num_augmentations):
    # Record the start time
    total_start_time = time.time()

    # Define augmentation transformations
    transform_flip = A.HorizontalFlip(p=1)
    transform_light = A.RandomBrightnessContrast(p=1)
    transform_rotate_left = A.ShiftScaleRotate(rotate_limit=20, shift_limit=0.0625, p=1)
    transform_rotate_right = A.ShiftScaleRotate(rotate_limit=-20, p=1)

    # Initialize a variable to store the total execution time
    total_execution_time = 0.0

    # Iterate through subfolders in the root folder
    for subfolder in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder)

        # Check if the item in the main folder is a directory
        if os.path.isdir(subfolder_path):
            print(f"Augmenting images in folder: {subfolder}")

            # Record the start time for the current subfolder
            start_time = time.time()

            # Iterate through image files in the subfolder
            for file in os.listdir(subfolder_path):
                try:
                    file_path = os.path.join(subfolder_path, file)
                    image = cv2.imread(file_path)

                    if image is None:
                        raise Exception("Invalid Image")

                    # Apply augmentations based on the 'num' parameter
                    augmented_images = []

                    if num_augmentations >= 2:
                        augmented_images.append(transform_flip(image=image)["image"])
                        augmented_images.append(transform_light(image=image)["image"])

                    if num_augmentations == 4:
                        augmented_images.append(transform_rotate_left(image=image)["image"])
                        augmented_images.append(transform_rotate_right(image=image)["image"])

                    file_name, file_ext = os.path.splitext(file)

                    # Save augmented images
                    for idx, augmented_image in enumerate(augmented_images):
                        augmented_file_name = f"{file_name}_aug{idx + 1}{file_ext}"
                        augmented_file_path = os.path.join(subfolder_path, augmented_file_name)
                        cv2.imwrite(augmented_file_path, cv2.cvtColor(augmented_image, cv2.COLOR_BGR2RGB))

                except Exception as e:
                    print(f"Error processing {file}: {e}")
                    # Handle the error or move the problematic file here if needed
                    continue

            # Record the end time for the current subfolder
            end_time = time.time()

            # Calculate the execution time for the current subfolder
            execution_time = end_time - start_time

            # Add the execution time of the current subfolder to the total execution time
            total_execution_time += execution_time

    # Record the end time for all subfolders
    total_end_time = time.time()

    # Calculate the total execution time for all subfolders
    total_execution_time = total_end_time - total_start_time

    # Print the total execution time
    print(f"Total time for processing all subfolders: {total_execution_time:.2f} seconds")



# Example usage:
root_folder = "Dataset"  # Replace 'MainFolder' with the path to your main directory
num_augmentations = 8  # You can change this to 2 if needed
augment_images_in_subfolders(root_folder, num_augmentations)
