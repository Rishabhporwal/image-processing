
import pandas as pd
import numpy as np
import cv2


#Read Image from CSV
def read_image_from_csv(image_pixel_csv_data):
    # Load the CSV file with image data
    csv_file = image_pixel_csv_data
    df = pd.read_csv(csv_file)
    return df



# Function to resize an image
def resize_image(csv_data_path):
    try:
        csv_data = read_image_from_csv(csv_data_path)
        image_data = csv_data.iloc[:, 1:].values
        depth_values = csv_data['depth'].values
    except Exception as e:
        print("Issue in Reading Image from CSV: ",e)

    # Resize the image to 150 pixels width
    try:
        image_width = 150
        resized_images = []
        for img_data in image_data:

            img = np.array(img_data, dtype=np.uint8).reshape(1, -1)
            img = cv2.resize(img, (image_width, 1), interpolation=cv2.INTER_LINEAR)
            resized_images.append(img)
        
        #Form image from an array
        resized_images = np.vstack(resized_images)
        df =  pd.DataFrame(resized_images )
        df["d"] = depth_values
        print("Image resize successfull")
        return df
    except Exception as e:
        print("Issue in image resizing")