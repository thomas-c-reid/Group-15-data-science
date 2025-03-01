import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
test_df = pd.read_csv('test.csv')
train_df = pd.read_csv('train.csv')

# Display the first 5 rows of the data
test_df.head()
train_df.head()


print(len(train_df))
print(len(test_df))

