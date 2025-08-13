import pandas as pd
import numpy as np
import os
from PIL import Image

mnist_dir = os.path.dirname(os.path.realpath(__file__))
output_dir = os.path.join(mnist_dir, 'output/png/train')
csv_file = os.path.join(mnist_dir, 'mnist_train.csv')

# Load CSV file
data_frame = pd.read_csv(csv_file, header=None)

os.makedirs(output_dir, exist_ok=True)

for col, row in data_frame.iterrows():
    label = row[0]
    pixels = row[1:].values.reshape(28, 28).astype(np.uint8)

    img = Image.fromarray(pixels)
    img.save(os.path.join(output_dir, f"number-{label}-index-{col}.png"))
