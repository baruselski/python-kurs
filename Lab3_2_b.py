# Laboratorium 3 Zadanie 2 Podpunkt 'b'

from datasets import load_dataset
import pandas

# Load dataset and convert to pandas dataframe
dataset = load_dataset("imodels/credit-card")
df = pandas.DataFrame(dataset['train'])

# Calculate correlation [-1.0, 1.0]
corr = df['age'].corr(df['limit_bal'])
print (corr)