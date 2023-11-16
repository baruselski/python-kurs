# Laboratorium 3 Zadanie 2 Podpunkt 'd'

from datasets import load_dataset
import pandas

# Load dataset and convert to pandas dataframe
dataset = load_dataset("imodels/credit-card")
df = pandas.DataFrame(dataset['train'])


# Add a new column with the sum of the selected columns
#bill_columns = ['bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6']
bill_columns = df.filter(like='bill_amt').columns
df['sum_of_bills'] = df[bill_columns].sum(axis=1)

print (df)