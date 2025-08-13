import pandas as pd

class Image:

    def __init__(csv_file, header=None):
        pass


train_data = pd.read_csv('mnist/mnist_train.csv', header=None)

print(train_data[:10])
