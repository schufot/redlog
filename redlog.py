import pandas as pd
import pyfiglet
from dateutil import parser

df = pd.read_csv("period_dates.txt", header=None)
df = df.apply(pd.to_datetime)

print(df.head())
print(pyfiglet.figlet_format("redlog"))