# Digit Recognizer

Here im trying to build a program that based on a PNG file can guess which number it is.

The goal is try to solve this using a CNN (Convolutional Neural Network). And maybe later
try to solve it with a Transformer.

## MNIST

The MNIST database (Mixed National Institute of Standards and Technology database)
is a large database of handwritten digits that is commonly used for training various
image processing systems.

The `mnist/` folder in this project contains `.py` files to be able to:

- Create csv to png
- Create png to csv
- Show image based on csv

Examples:

```shell
# setup
unzip mnist/mnist_test.csv.zip -d mnist
unzip mnist/mnist_train.csv.zip -d mnist

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create png files from csv file
python mnist/csv_to_png.py

# Create csv file from png files
python mnist/png_to_csv.py

# Show image based on csv file (look in the python file to change which index to show)
python mnist/show_img_from_csv.py
```
