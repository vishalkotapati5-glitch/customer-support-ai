import pandas as pd

df = pd.read_csv("data/tickets.csv")

print("First 5 tickets:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nCategory counts:")
print(df["category"].value_counts())

print("\nPriority counts:")
print(df["priority"].value_counts())