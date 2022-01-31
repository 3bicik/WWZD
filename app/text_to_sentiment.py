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

classes = ["Happy", "Sad", "Love", "Anger"]
coordinates = ["X", "Y"]

def prep_lines_dataframe():
    lines = pandas.read_csv('data/simpsons_dataset.csv')
    data = numpy.zeros((len(lines),2))
    lines['data'] = data.tolist()
    lines['raw_character_text'] = lines['raw_character_text'].astype(str)
    lines['spoken_words'] = lines['spoken_words'].astype(str)
    lines['data'] = lines['data'].astype(object)

    return lines

def prep_episode_dataframe(filename):
    lines = pandas.read_csv(f'data/csv/{filename}.csv')
    data = numpy.zeros((len(lines),2))
    lines['data'] = data.tolist()
    lines['raw_character_text'] = lines['raw_character_text'].astype(str)
    lines['spoken_words'] = lines['spoken_words'].astype(str)
    lines['data'] = lines['data'].astype(object)

    return lines

def process_data(lines):
    with open('text_to_sentiment/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    lines_text = lines['spoken_words']

    sequences_test = tokenizer.texts_to_sequences(lines_text)
    data_int_t = pad_sequences(sequences_test, padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    return model.predict(data_test, verbose='1')


def calculate_personality(lines, threshold):
    name_temp = ''
    vec_temp = numpy.zeros(2)
    times = 0

    for index, row in lines.sort_values(by=['raw_character_text']).iterrows():
        if(index == 0):
            name_temp = row['raw_character_text']
        
        if(row['raw_character_text'] == name_temp):
            pred = row['data'].argmax(axis=-1)
            pred_prob = row['data'][pred]

            if(pred==0):
                vec_temp[0] += pred_prob**2
            if(pred==1):
                vec_temp[0] -= pred_prob**2
            if(pred==2):
                vec_temp[1] += pred_prob**2
            if(pred==3):
                vec_temp[1] -= pred_prob**2

            # vec_temp += row['data']
            times += 1
        else:
            if(times >= threshold):
                Character(name=name_temp, data=vec_temp/times, number_of_lines=times).save()
            name_temp = row['raw_character_text']
            vec_temp = numpy.zeros(2)
            pred = row['data'].argmax(axis=-1)
            pred_prob = row['data'][pred]
            
            if(pred==0):
                vec_temp[0] += pred_prob**2
            if(pred==1):
                vec_temp[0] -= pred_prob**2
            if(pred==2):
                vec_temp[1] += pred_prob**2
            if(pred==3):
                vec_temp[1] -= pred_prob**2

            # vec_temp = row['data']
            times = 1


def predict():
    lines = prep_lines_dataframe()
    y_prob = process_data(lines)

    for n, prediction in enumerate(y_prob):
        prediction = numpy.delete(prediction, 0, 0)
        lines.at[n, 'data'] = prediction

    calculate_personality(lines.sort_values(by=['raw_character_text']), 200)

def sample_predict():
    sample_lines = prep_lines_dataframe().head(200)
    y_prob = process_data(sample_lines)

    for n, prediction in enumerate(y_prob):
        prediction = numpy.delete(prediction, 0, 0)
        sample_lines.at[n, 'data'] = prediction

    calculate_personality(sample_lines.sort_values(by=['raw_character_text']), 5)

def pred(filename):
    sample_lines = prep_episode_dataframe(filename)
    y_prob = process_data(sample_lines)

    for n, prediction in enumerate(y_prob):
        prediction = numpy.delete(prediction, 0, 0)
        sample_lines.at[n, 'data'] = prediction

    calculate_personality(sample_lines.sort_values(by=['raw_character_text']), 5)

