import pandas
from .models import Character, Line

def load_csv_to_database():
    Line.objects.all().delete()
    Character.objects.all().delete()
    data_frame = pandas.read_csv('data/simpsons_dataset.csv')
    print(data_frame.size)
    # for index, row in data_frame.iterrows():
    #     new_line = Line(name=row['raw_character_text'], text=row['spoken_words'], emotion='')
    #     new_line.save()
    # characters = pandas.DataFrame({'raw_character_text':data_frame.raw_character_text.unique()})
    # for index, row in characters.iterrows():
    #     new_character = Character(name=row['raw_character_text'], personality='neutral')
    #     new_character.save()