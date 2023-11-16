# Laboratorium 3 Zadanie 2 Podpunkt 'a'

from datasets import load_dataset
import pandas

# Load dataset and convert to pandas dataframe
dataset = load_dataset("imodels/credit-card")
df = pandas.DataFrame(dataset['train'])

# Remove duplicates based on all columns
df_no_duplicates = df.drop_duplicates()

#print(df_no_duplicates.to_string()) 