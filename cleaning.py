import pandas as pd
import re
import string
import data

eng_hin_data = pd.read_table("data/hin.txt",names=['English','Hindi','value']).drop('value',axis=1)

print(eng_hin_data.head())