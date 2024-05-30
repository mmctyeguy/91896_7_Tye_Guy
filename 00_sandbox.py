import pandas as pd

from tabulate import tabulate
df = pd.DataFrame({'Text': ['abcdef', 'x'], 'Value': [12.34, 4.2]})
print(tabulate(df, showindex=False, headers=df.columns))
