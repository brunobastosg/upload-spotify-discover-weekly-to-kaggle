import pandas as pd

# run download-playlist-from-spotify.py to get this csv
df_this_week = pd.read_csv('output/this-weeks-playlist.csv')

# run command: "kaggle datasets download brunobastosg/my-spotify-discover-weekly -f my-spotify-discover-weekly.csv -p dataset" to get this csv
df_entire_dataset = pd.read_csv('dataset/my-spotify-discover-weekly.csv')

pd.concat([df_entire_dataset, df_this_week]).drop_duplicates().sort_values(by=['Added At'], ascending=False).to_csv('my-spotify-discover-weekly.csv', index=None)
