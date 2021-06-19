from cleaning import textcleaner
import pandas as pd
import numpy as np
import re
import string
import data
import cleaning
import vocab
import random
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

eng_hin_data = pd.read_table("data/hin.txt",names=['English','Hindi','value']).drop('value',axis=1)

eng_hin_data_cleaned = cleaning.textcleaner(eng_hin_data)

eng_vocab,max_len_eng,hin_vocab,max_len_hin = vocab.create_vocab(eng_hin_data_cleaned)

num_enc_tokens,num_de_tokens,in_token_index,reverse_in_index,tar_token_index,reverse_tar_index = vocab.create_tokens(eng_vocab,hin_vocab)

eng_hin_data_cleaned = shuffle(eng_hin_data_cleaned)

# Train - Test Split
X_train, X_test, y_train, y_test = train_test_split(eng_hin_data_cleaned.English, eng_hin_data_cleaned.Hindi, test_size = 0.1)

def generate_batch(X = X_train, y = y_train, batch_size = 128):
    ''' Generate a batch of data '''
    while True:
        for j in range(0, len(X), batch_size):
            encoder_input_data = np.zeros((batch_size, max_len_eng),dtype='float32')
            decoder_input_data = np.zeros((batch_size, max_len_hin),dtype='float32')
            decoder_target_data = np.zeros((batch_size, max_len_hin, num_de_tokens),dtype='float32')
            for i, (input_text, target_text) in enumerate(zip(X[j:j+batch_size], y[j:j+batch_size])):
                for t, word in enumerate(input_text.split()):
                    encoder_input_data[i, t] = in_token_index[word] # encoder input seq
                for t, word in enumerate(target_text.split()):
                    if t<len(target_text.split())-1:
                        decoder_input_data[i, t] = tar_token_index[word] # decoder input seq
                    if t>0:
                        # decoder target sequence (one hot encoded)
                        # does not include the START_ token
                        # Offset by one timestep
                        decoder_target_data[i, t - 1, tar_token_index[word]] = 1.
            yield([encoder_input_data, decoder_input_data], decoder_target_data)