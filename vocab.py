import pandas as pd
import numpy as np

def create_vocab(data):
    
    all_eng_words=set()
    for eng in engmar_df_40k['English'] :
        for word in eng.split():
            if word not in all_eng_words:
                all_eng_words.add(word)
                
    all_marathi_words=set()
    for mar in engmar_df_40k['Marathi']:
        for word in mar.split():
            if word not in all_marathi_words:
                all_marathi_words.add(word)

    return sorted(all_eng_words),sorted(all_marathi_words))

def create_tokens(enc_vocab,dec_vocab):
   
    num_encoder_tokens = len(enc_vocab)
    num_decoder_tokens = len(dec_vocab)
    num_decoder_tokens += 1 # For zero padding
    input_token_index = dict([(word, i+1) for i, word in enumerate(enc_vocab)])
    target_token_index = dict([(word, i+1) for i, word in enumerate(dec_vocab)])
    reverse_input_char_index = dict((i, word) for word, i in input_token_index.items())
    reverse_target_char_index = dict((i, word) for word, i in target_token_index.items())

    return num_encoder_tokens,num_decoder_tokens,input_token_index,reverse_input_char_index,target_token_index,reverse_target_char_index
