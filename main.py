from cleaning import textcleaner
import pandas as pd
import re
import string
import data
import cleaning
import vocab

eng_hin_data = pd.read_table("data/hin.txt",names=['English','Hindi','value']).drop('value',axis=1)

eng_hin_data_cleaned = cleaning.textcleaner(eng_hin_data)

eng_vocab,max_len_eng,hin_vocab,max_len_hin = vocab.create_vocab(eng_hin_data_cleaned)

