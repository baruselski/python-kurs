# Laboratorium 3 Zadanie 2 Podpunkt 'c'

from datasets import load_dataset
import pandas

# Load dataset and convert to pandas dataframe
dataset = load_dataset("imodels/credit-card")
df = pandas.DataFrame(dataset['train'])