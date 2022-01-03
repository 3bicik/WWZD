import tensorflow
import numpy
from tensorflow import keras
from keras.models import load_model
import pandas
import itertools, pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# from .models import Character, Line
from .models import Character

MAX_NB_WORDS = 56000 # max no. of words for tokenizer
MAX_SEQUENCE_LENGTH = 30 # max length of text (words) including padding

model = keras.models.load_model("text_to_sentiment/checkpoint-0.6017.h5")

classes = ["Neutral", "Happy", "Sad", "Love", "Anger"]


def prep_dataframes():
    lines = pandas.read_csv('data/simpsons_dataset.csv')
    sentiment = numpy.zeros(len(lines))
    lines['sentiment'] = sentiment.tolist()
    lines['raw_character_text'] = lines['raw_character_text'].astype(str)
    lines['spoken_words'] = lines['spoken_words'].astype(str)
    lines['sentiment'] = lines['sentiment'].astype(object)

    characters = pandas.DataFrame({'raw_character_text':lines.raw_character_text.unique()})
    sentiment = numpy.zeros((len(characters),5))
    characters['sentiment'] = sentiment.tolist()
    number_of_lines = numpy.zeros((len(characters),1))
    characters['number_of_lines'] = number_of_lines.tolist()
    characters['sentiment'] = characters['sentiment'].astype(object)
    characters['number_of_lines'] = characters['number_of_lines'].astype(object)

    return lines, characters



def predict():
    lines, characters = prep_dataframes()
    lines_text = lines['spoken_words']
    
    sample_lines = lines.head(10)
    sample_lines_text = sample_lines['spoken_words']

    sample_characters = pandas.DataFrame({'raw_character_text':sample_lines.raw_character_text.unique()})
    sentiment = numpy.zeros((len(sample_characters),5))
    sample_characters['sentiment'] = sentiment.tolist()
    number_of_lines = numpy.zeros((len(sample_characters),1))
    sample_characters['number_of_lines'] = number_of_lines.tolist()
    sample_characters['sentiment'] = sample_characters['sentiment'].astype('object')
    sample_characters['number_of_lines'] = sample_characters['number_of_lines'].astype('object')

    with open('text_to_sentiment/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    sequences_test = tokenizer.texts_to_sequences(sample_lines_text)
    data_int_t = pad_sequences(sequences_test, padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    y_prob = model.predict(data_test, verbose='1')

    for n, prediction in enumerate(y_prob):
        pred = y_prob.argmax(axis=-1)[n]
        sample_lines.at[n, 'sentiment'] = prediction

    sample_lines.sort_values(by=['raw_character_text'])  

    name_temp = ''
    vec_temp = numpy.zeros(5)
    times = 0

    Character.objects.all().delete()

    for index, row in sample_lines.sort_values(by=['raw_character_text']).iterrows():
        if(index == 0):
            name_temp = row['raw_character_text']
        
        if(row['raw_character_text'] == name_temp):
            vec_temp += row['sentiment']
            times += 1
        else:
            Character(name=name_temp, sentiment=vec_temp/times, number_of_lines=times).save()

            name_temp = row['raw_character_text']
            vec_temp = row['sentiment']
            times = 1

        
    
     


def pred():
    lines, characters = prep_dataframes()
    lines_text = lines['spoken_words']

    
    sample_lines = lines.head(10)
    sample_lines_text = sample_lines['spoken_words']

    sample_characters = pandas.DataFrame({'raw_character_text':sample_lines.raw_character_text.unique()})
    sample_characters['sentiment'] = numpy.full_like(sample_characters['raw_character_text'], '')
    sample_characters['number_of_lines'] = numpy.zeros_like(sample_characters['sentiment'])
    # for index, row in sample_lines.iterrows():
    with open('text_to_sentiment/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    sequences_test = tokenizer.texts_to_sequences(sample_lines_text)
    data_int_t = pad_sequences(sequences_test, padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    y_prob = model.predict(data_test, verbose='1')

    for n, prediction in enumerate(y_prob):
        pred = y_prob.argmax(axis=-1)[n]
        sample_lines.at[n, 'sentiment'] = prediction

    sample_lines.sort_values(by=['raw_character_text'])

    # name_temp = ''

    # for n, line in enumerate(sample_lines):
    #     if(line['raw_character_text'] == name_temp):