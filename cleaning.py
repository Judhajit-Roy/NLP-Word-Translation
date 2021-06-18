import pandas as pd
import re
import string
import data

def textcleaner(eng_hin_data):

    # Lowercase all characters
    eng_hin_data.English=eng_hin_data.English.apply(lambda x: x.lower())

    # Remove quotes
    eng_hin_data.English=eng_hin_data.English.apply(lambda x: re.sub("'", '', x))
    eng_hin_data.Hindi=eng_hin_data.Hindi.apply(lambda x: re.sub("'", '', x))
    exclude = set(string.punctuation) # Set of all special characters

    # Remove all the special characters
    eng_hin_data.English=eng_hin_data.English.apply(lambda x: ''.join(ch for ch in x if ch not in exclude))
    eng_hin_data.Hindi=eng_hin_data.Hindi.apply(lambda x: ''.join(ch for ch in x if ch not in exclude))

    # Remove all numbers from text
    digits = '1234567890'
    remove_digits = str.maketrans('', '', digits)
    eng_hin_data.English=eng_hin_data.English.apply(lambda x: x.translate(remove_digits))
    eng_hin_data.Hindi = eng_hin_data.Hindi.apply(lambda x: re.sub("[२३०८१५७९४६]", "", x))

    # Remove extra spaces
    eng_hin_data.English=eng_hin_data.English.apply(lambda x: x.strip())
    eng_hin_data.Hindi=eng_hin_data.Hindi.apply(lambda x: x.strip())
    eng_hin_data.English=eng_hin_data.English.apply(lambda x: re.sub(" +", " ", x))
    eng_hin_data.Hindi=eng_hin_data.Hindi.apply(lambda x: re.sub(" +", " ", x))

    # Add start and end tokens to target sequences
    eng_hin_data.Hindi = eng_hin_data.Hindi.apply(lambda x : 'START_ '+ x + ' _END')

    return eng_hin_data


