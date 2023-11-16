from datasets import load_dataset
import pandas as pd
from tabulate import tabulate

# Load the dataset
dataset = load_dataset("imodels/credit-card")
df = pd.DataFrame(dataset['train'])

# Rename the education columns based on the provided key
education_mapping = {
    0: 'graduate school',
    1: 'university',
    2: 'high school',
    3: 'others',
    4: 'unknown',
    5: 'unknown',
    6: 'unknown'
}

df = df.rename(columns={f'education:{i}': f'Education:{education_mapping[i]}' for i in range(7) if f'education:{i}' in df.columns})

# Find the 10 oldest clients
oldest_clients = df.nlargest(10, 'age')

# Sum all education
oldest_clients['completed_education'] = oldest_clients.filter(like='Education:').sum(axis=1)

# Select only the required columns
selected_columns = ['limit_bal', 'age', 'Education:graduate school', 'Education:university', 'Education:high school', 'Education:others', 'Education:unknown', 'completed_education']
oldest_clients = oldest_clients[selected_columns]

# Print the resulting table
print(tabulate(oldest_clients, headers = 'keys', tablefmt = 'psql'))
