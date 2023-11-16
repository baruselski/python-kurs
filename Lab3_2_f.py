# Laboratorium 3 Zadanie 2 Podpunkt 'f'

from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset = load_dataset("imodels/credit-card")
df = pd.DataFrame(dataset['train'])

# Set up subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 12))
fig.suptitle('Credit Card Dataset Analysis', fontsize=16)

# Plot credit limit histogram
axes[0].hist(df['limit_bal'], bins=20, color='skyblue', edgecolor='black')
axes[0].set_title('Histogram of Credit Limit')
axes[0].set_xlabel('Credit Limit')
axes[0].set_ylabel('Frequency')

# Plot age histogram
axes[1].hist(df['age'], bins=20, color='salmon', edgecolor='black')
axes[1].set_title('Histogram of Age')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Frequency')

# Scatter plot of credit limit vs. age
axes[2].scatter(df['age'], df['limit_bal'], color='green', alpha=0.5)
axes[2].set_title('Scatter Plot of Age vs. Credit Limit')
axes[2].set_xlabel('Age')
axes[2].set_ylabel('Credit Limit')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()