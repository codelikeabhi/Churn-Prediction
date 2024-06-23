import pandas as pd

data = pd.read_parquet('churn_data_regulated.parquet')

print(data['tenure'])