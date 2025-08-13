import os
import numpy as np
from PIL import Image
import pandas as pd

mnist_dir = os.path.dirname(os.path.realpath(__file__))
input_dir = os.path.join(mnist_dir, 'output/png/train')
output_file = os.path.join(mnist_dir, 'output/csv/png_to_csv.csv')

rows = []

for index, file in enumerate(os.listdir(input_dir)[:10]):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_dir, file)

        # Load image file
        img = Image.open(img_path)
        img = img.resize((28,28)) # ensure 28x28
        pixels = np.array(img).flatten()

        # Add row: label + flatten pixels
        row = np.insert(pixels, 0, index)
        rows.append(row)

# Save to CSV
df = pd.DataFrame(rows)
os.makedirs(os.path.dirname(output_file), exist_ok=True)
df.to_csv(output_file, index=False, header=False)
