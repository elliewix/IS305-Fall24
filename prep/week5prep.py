import csv
import pathlib


with open('query.csv', 'rt', encoding= 'utf-8') as infile:
    headers, *data = csv.reader(infile)

new_data = {}
dupes = []

for r in data:
    url = r[0]
    horse_id = url.split('/')[-1]
    # print(horse_id)
    content = "\n".join(r)
    if not horse_id in new_data:
        new_data[horse_id] = content
    else:
        dupes.append(r)

content_target = pathlib.Path('content')
content_target.mkdir(exist_ok=True)
for horse_id, content in new_data.items():
    p = pathlib.Path(horse_id + '.txt')
    full_p = content_target / p
    full_p.write_text(content)

