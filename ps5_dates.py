from glob import glob

import json
import pendulum

files = glob("/Volumes/USB/PS5/CREATE/**/**/*.jpg")

games = {}

for file in files:
    file = file.replace('/Volumes/USB/PS5/CREATE/Screenshots/', '')
    file = file.replace('/Volumes/USB/PS5/CREATE/Video Clips/', '')
    title, ext = file.split('/')
    ext = ext.replace(title + '_', '').replace('.jpg', '')

    if title == 'FINAL FANTASY XIV':
        continue

    timestamp = pendulum.from_format(ext, "YYYYMMDDHHmmss", tz="Pacific/Auckland")

    if title not in games.keys():
        games[title] = set()

    games[title].add(timestamp.to_date_string())

for game in games:
    games[game] = sorted(list(games[game]))
    
    print(game)
    for date in games[game]:
        print(date)
    
    print()
    print("---")
    print()
