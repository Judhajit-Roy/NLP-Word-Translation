import pandas as pd
import re
import string
import data

def textcleaner(engmar_df):

    engmar_df['eng_len'] = engmar_df['English'].apply(lambda x: len(x.split()))
    engmar_df['mar_len'] = engmar_df['Marathi'].apply(lambda x: len(x.split()))

    engmar_df_40k = engmar_df[(engmar_df['eng_len'] <= 20) & (engmar_df['eng_len'] > 2)]

    # remove special characters english and marathi
    exclude = set(string.punctuation)
    exclude.add('।')
    # enghin_df_30k['Hindi'] = enghin_df_30k['Hindi'].apply(lambda x:' '.join(re.sub("(%{[A-Za-z0-9]+)|(&[A-Za-z0-9]+)", " ", x).split()))
    engmar_df_40k['Marathi'] = engmar_df_40k['Marathi'].apply(lambda x: ''.join([i for i in x if i not in exclude]))

    # enghin_df_30k['English'] = enghin_df_30k['English'].apply(lambda x:' '.join(re.sub("(%{[A-Za-z0-9]+)|(&[A-Za-z0-9]+)", " ", x).split()))
    engmar_df_40k['English'] = engmar_df_40k['English'].apply(lambda x: ''.join([i for i in x if i not in exclude]))

    # Lowercase all characters
    engmar_df_40k['English'] = engmar_df_40k['English'].apply(lambda x: x.lower())
    engmar_df_40k['Marathi'] = engmar_df_40k['Marathi'].apply(lambda x: x.lower())


    # Add start and end tokens to target sequences
    engmar_df_40k['Marathi'] = engmar_df_40k['Marathi'].apply(lambda x : '<START> '+ x + ' <END>')

    return engmar_df_40k


