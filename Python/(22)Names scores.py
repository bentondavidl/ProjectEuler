with open(r'data files\p022_names.txt') as file:
    names = file.read().replace('"', '').split(',')

names.sort()

print(sum([sum([ord(x)-64 for x in name])*(i+1)
           for i, name in enumerate(names)]))
