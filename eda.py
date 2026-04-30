import pandas as pd
import matplotlib.pyplot as plt

print("START")

# load dataset
df = pd.read_csv("cleaned_customers.csv")

# Basic info
print("\nDataset Info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

# Segment count
print("\nSegment Count:")
print(df['segment'].value_counts())

# State count
print("\nState Count:")
print(df['state'].value_counts())

# Graphs
df['segment'].value_counts().plot(kind='bar', title='Customer Segments')
plt.show()

df['state'].value_counts().head(10).plot(kind='bar', title='Top States')
plt.show()

# Business Questions
print("\n--- Business Questions ---")

print("\nMost customers in segment:")
print(df['segment'].value_counts().head(1))

print("\nTop state:")
print(df['state'].value_counts().head(1))

print("\nTop city:")
print(df['city'].value_counts().head(1))

print("\nTotal customers:")
print(len(df))

print("END")