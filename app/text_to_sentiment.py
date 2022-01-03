import tensorflow
import numpy
from tensorflow import keras
from keras.models import load_model
import pandas
import itertools, pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from .models import Character

MAX_NB_WORDS = 56000 # max no. of words for tokenizer
MAX_SEQUENCE_LENGTH = 30 # max length of text (words) including padding

model = keras.models.load_model("text_to_sentiment/checkpoint-0.6017.h5")

classes = ["Neutral", "Happy", "Sad", "Love", "Anger"]


def prep_lines_dataframe():
    lines = pandas.read_csv('data/simpsons_dataset.csv')
    sentiment = numpy.zeros((len(lines),5))
    lines['sentiment'] = sentiment.tolist()
    lines['raw_character_text'] = lines['raw_character_text'].astype(str)
    lines['spoken_words'] = lines['spoken_words'].astype(str)
    lines['sentiment'] = lines['sentiment'].astype(object)

    return lines

def process_data(lines):
    with open('text_to_sentiment/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    lines_text = lines['spoken_words']

    sequences_test = tokenizer.texts_to_sequences(lines_text)
    data_int_t = pad_sequences(sequences_test, padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    return model.predict(data_test, verbose='1')


def calculate_averages(lines, threshold):
    name_temp = ''
    vec_temp = numpy.zeros(5)
    times = 0

    for index, row in lines.sort_values(by=['raw_character_text']).iterrows():
        if(index == 0):
            name_temp = row['raw_character_text']
        
        if(row['raw_character_text'] == name_temp):
            vec_temp += row['sentiment']
            times += 1
        else:
            if(times >= threshold):
                Character(name=name_temp, sentiment=vec_temp/times, number_of_lines=times).save()
            name_temp = row['raw_character_text']
            vec_temp = row['sentiment']
            times = 1


def predict():
    lines = prep_lines_dataframe()
    y_prob = process_data(lines)

    for n, prediction in enumerate(y_prob):
        lines.at[n, 'sentiment'] = prediction

    calculate_averages(lines.sort_values(by=['raw_character_text']), 200)

def sample_predict():
    sample_lines = prep_lines_dataframe().head(200)
    y_prob = process_data(sample_lines)

    for n, prediction in enumerate(y_prob):
        sample_lines.at[n, 'sentiment'] = prediction

    calculate_averages(sample_lines.sort_values(by=['raw_character_text']), 5)

