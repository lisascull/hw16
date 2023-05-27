#1
import pickle
files = [
    {'ключ1': 'значення1', 'ключ2': 'значення2'},
    {'ключ1': 'значення3', 'ключ2': 'значення4'},
    {'ключ1': 'значення5', 'ключ2': 'значення6'}
]
with open('files.pkl', 'wb') as file:
    pickle.dump(files, file)
#2
import json

A = {'key': 1}
B = {'key1': 2}
C = {}

for key, unite in A.items():
    C[key] = unite

for key, unite in B.items():
    if key in C:
        if isinstance(C[key], list):
            C[key].append(unite)
        else:
            C[key] = [C[key], unite]
    else:
        C[key] = unite
with open('result.json', 'w') as file:
    json.dump(C, file)
