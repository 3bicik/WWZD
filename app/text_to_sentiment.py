import tensorflow
import numpy
from tensorflow import keras
from keras.models import load_model
import pandas
import itertools, pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from .models import Character, Line

MAX_NB_WORDS = 56000 # max no. of words for tokenizer
MAX_SEQUENCE_LENGTH = 30 # max length of text (words) including padding

model = keras.models.load_model("text_to_sentiment/checkpoint-0.6017.h5")

classes = ["Neutral", "Happy", "Sad", "Love", "Anger"]
text = [
        "How rude",
        "I'm gonna be sick",
        "I hate you",
        "I love her",
        "That's great",
        "I'm delighted",
]

def prep_dataframes():
    lines = pandas.read_csv('data/simpsons_dataset.csv')
    lines['sentiment'] = numpy.NaN
    lines.raw_character_text=lines.raw_character_text.astype(str)
    lines.spoken_words=lines.spoken_words.astype(str)
    lines.sentiment=lines.sentiment.astype(str)

    characters = pandas.DataFrame({'raw_character_text':lines.raw_character_text.unique()})
    characters['sentiment'] = numpy.full_like(characters['raw_character_text'], '')
    characters['number_of_lines'] = numpy.zeros_like(characters['sentiment'])

    return lines, characters


def predict():
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

        print("Vector: ", prediction)
        print(lines_text[n],"\nPREDICTION:",classes[pred], "\n")

