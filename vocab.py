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

    return sorted(list(eng_vocab)),max_len_eng,sorted(list(hin_vocab)),max_len_hin

def create_tokens(enc_vocab,dec_vocab):
   
    num_encoder_tokens = len(enc_vocab)
    num_decoder_tokens = len(dec_vocab)
    num_decoder_tokens += 1 # For zero padding
    input_token_index = dict([(word, i+1) for i, word in enumerate(enc_vocab)])
    target_token_index = dict([(word, i+1) for i, word in enumerate(dec_vocab)])
    reverse_input_char_index = dict((i, word) for word, i in input_token_index.items())
    reverse_target_char_index = dict((i, word) for word, i in target_token_index.items())

    return num_encoder_tokens,num_decoder_tokens,input_token_index,reverse_input_char_index,target_token_index,reverse_target_char_index