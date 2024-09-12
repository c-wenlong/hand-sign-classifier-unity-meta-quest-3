import pandas as pd
import os
import csv

# Example array of 41 values (a single row of data)
sample =[0.0, 0.0, 0.3235294117647059, 0.22941176470588234, 0.5941176470588235, 0.4470588235294118, 0.7941176470588235, 0.6235294117647059, 1.0, 0.7470588235294118, 0.6470588235294118, 0.4, 0.8176470588235294, 0.5647058823529412, 0.9058823529411765, 0.6705882352941176, 0.9647058823529412, 0.7235294117647059, 0.48823529411764705, 0.3941176470588235, 0.6529411764705882, 0.5411764705882353, 0.7529411764705882, 0.6058823529411764, 0.8235294117647058, 0.6588235294117647, 0.35294117647058826, 0.3941176470588235, 0.48823529411764705, 0.49411764705882355, 0.5882352941176471, 0.5529411764705883, 0.6470588235294118, 0.611764705882353, 0.23529411764705882, 0.4117647058823529, 0.37058823529411766, 0.4823529411764706, 0.45294117647058824, 0.5117647058823529, 0.49411764705882355, 0.5294117647058824,1]

# read file
def read_hand_joint_data_from_csv(file_path="./hand_joint_data.csv"):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return None

# Function to append an array to the CSV file
def append_data_to_csv(data_to_add, file_path="../handsign_classifier/handsign_classifier.csv"):
    # Load the existing CSV file
    df = pd.read_csv(file_path)

    # Ensure the data_to_add matches the number of columns in the CSV
    if len(data_to_add) != len(df.columns):
        raise ValueError(f"Shape mismatch: data_to_add has {len(data_to_add)} values, but the file expects {len(df.columns)} columns.")
    
    # Convert the array into a DataFrame (single row)
    new_data = pd.DataFrame([data_to_add], columns=df.columns)  # Wrap the list in another list to make it a 2D array
    
    # Append the new data as a row
    df = pd.concat([df, new_data], ignore_index=True)
    
    # Save back to the CSV file
    df.to_csv(file_path, index=False)

def append_batch_to_csv(file_path, data_batch):
    """
    Appends a batch of data (a list of lists) to a CSV file.
    
    Args:
    - file_path (str): The path to the CSV file.
    - data_batch (list of lists): The batch of data to append, where each list is a row.
    """
    # Open the file in append mode, and set newline='' to avoid extra blank rows
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the batch of lists (rows) to the CSV
        writer.writerows(data_batch)
