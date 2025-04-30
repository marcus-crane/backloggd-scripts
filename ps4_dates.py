from glob import glob

import json
import pendulum

files = glob("/Volumes/USB/PS4/SHARE/**/**/*.jpg")

games = {}

for file in files:
    file = file.replace('/Volumes/USB/PS4/SHARE/Screenshots/', '')
    file = file.replace('/Volumes/USB/PS4/SHARE/Video Clips/', '')

    if 'Picture_' in file:
        continue
    title, ext = file.split('/')
    ext = ext.replace(title + '_', '').replace('.jpg', '')
    
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
