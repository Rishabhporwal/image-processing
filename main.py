import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
import sqlite3
from flask import Flask
from matplotlib import cm
#Inbuilt Packages
from utils.image_resize import resize_image
from db.image_into_db import store_image_array_into_db,fetch_data_from_db,calculate_min_max_depth


# Step 3: API Development with FastAPI
app = Flask(__name__)
@app.get("/")
def get_image_frames():
    try:
        #Perfrom Image read and resize operation as per the instruction within challenge
        image_csv_path = r'data/AIQ-Data.csv'
        resized_img_df = resize_image(image_csv_path)


        #Image into Databse(image_database.db) within table(image_data)
        store_image_array_into_db(resized_img_df)

        #Filterout depth values
        min_max_depth = calculate_min_max_depth()
        depth_min = min_max_depth.get("min_depth")
        depth_max = min_max_depth.get("max_depth")
        filtered_frames = fetch_data_from_db(depth_min,depth_max)
        
        #AppExtracted Image Frames
        img_frames = filtered_frames.values
        img_frames = img_frames[:,:-1]
        img_frames = img_frames.astype(np.uint8)
        print("img>>>>",img_frames.shape)

        # Apply the custom color map to the image array
        color_map = plt.get_cmap('gist_rainbow')
        # Apply the colormap like a function to any array:
        color_mapped_frames = color_map (img_frames)
        create_img = Image.fromarray((color_mapped_frames[:, :, :3] * 255).astype(np.uint8))
        create_img.save('output/colored_frames.png')
        return "Successfully generate the response"
    except:
        return "Issue in generating final response"


if __name__ == '__main__':
    app.run("0.0.0.0", 8080)