import pathlib

with open('sibling.txt','rt', encoding='utf-8') as infile:
    text = infile.read()

print(text)

# with open('this.txt', 'rt', encoding='utf-8') as infile:
# won't work because it doesn't know about this.txt
with open('fakedata/this.txt', 'rt', encoding='utf-8') as infile:
    text = infile.read()
# print(text)

# we can make this all better

data_dir = pathlib.Path('fakedata')
print(data_dir, data_dir.exists())

p = pathlib.Path('this.txt')
print(p, type(p))
print(p.exists())

full_file = data_dir / p
print(full_file, full_file.exists())

print(full_file.name, full_file.stem, full_file.suffix)
print(full_file.absolute())

data_files = data_dir.glob('*.dat') # takes a sting, unix like

print(list(data_files))

for p in data_dir.glob('*'):
    print(p.absolute())

