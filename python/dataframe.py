import pandas as pd; # type: ignore

songs = {
    'Album': ["Thriller", "Let It Be", "The Dark Side of the Moon", "The Bodyguard"],
    'Released': [1982, 1970, 1973, 1992],
    'Length': ['00:42:19', '00:40:10', '00:42:49', '00:57:44'],
    'Artist': ['Michael Jackson', "The Beatles", "Pink Floyd", "Whitney Houston"]
}

# Build the DataFrame (rows x columns)
songs_frame = pd.DataFrame(songs)

# Selected DataFrame
length_frame = songs_frame[['Album' ,'Length']]

# Specific Cell
year_released = songs_frame.iloc[0, 3] # 1982

# Indexing
songs_frame.index = ['a', 'b', 'c', 'd']

# print(year_released)
print(songs_frame.head())
print(songs_frame.loc['a', 'Artist']) # Michael Jackson