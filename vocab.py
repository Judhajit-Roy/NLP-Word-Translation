import pandas as pd
import numpy as np

def create_vocab(data):
    
    eng_vocab = set()
    eng_line_length = []
    for line in data.English:
        for word in line.split():
            if word not in eng_vocab:
                eng_vocab.add(word)
        eng_line_length.append(len(line.split(' ')))

    max_len_eng = np.max(eng_line_length)

    hin_vocab = set()
    hin_line_length = []
    for line in data.Hindi:
        for word in line.split():
            if word not in hin_vocab:
                hin_vocab.add(word)
        hin_line_length.append(len(line.split(' ')))
    
    max_len_hin = np.max(hin_line_length)

    return eng_vocab,max_len_eng,hin_vocab,max_len_hin
