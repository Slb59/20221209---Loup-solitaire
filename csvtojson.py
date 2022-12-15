from csv import DictReader
import json

path = "data/loup.csv"
data = {}

with open(path, 'r', encoding='utf-8', errors='replace') as csv_file:

    csv_reader = DictReader(csv_file, delimiter=';')

    for row in csv_reader:
        print(row)
        key = row['Fiche']
        data[key] = row

        with open('data/chapters.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(data, indent=4, ensure_ascii=False))