import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

mnist_dir = os.path.dirname(os.path.realpath(__file__))

csv_filename = 'mnist_test.csv'
csv_file_path = os.path.join(mnist_dir, csv_filename)

df = pd.read_csv(csv_file_path, header=None)
labels = df.iloc[:, 0].values
pixels = df.iloc[:, 1:].values

index_to_show = 0
image = pixels[index_to_show].reshape(28, 28)
plt.imshow(image, cmap='gray')
plt.title(f"Label: {labels[index_to_show]}")
plt.show()

