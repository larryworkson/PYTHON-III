import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv('files/sentimentos.csv')

print(df.head(10))

# python ex013-RL-amazon-reviews.py