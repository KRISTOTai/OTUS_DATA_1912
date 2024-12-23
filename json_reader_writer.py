import csv
import json
from files import JSON_FILE_PATH, JSON_FILE_RESULT
from files import JSON_FILE_FORMAT
from files import CSV_FILE_PATH
import itertools

with open(JSON_FILE_FORMAT, "r") as f:
    format_read = json.load(f)
keys = (list(itertools.chain(*format_read)))

with open(JSON_FILE_PATH, "r") as f:
    path_read = json.load(f)

with open(CSV_FILE_PATH, newline='') as f:
    books_read = csv.reader(f)
    header = next(books_read)
    list_of_books = []
    for row in books_read:
        dicts = dict(zip(header, row))
        list_of_books.append(dicts)

# Получение списка списков из необходимых данных
list_of_lists = []
for client in path_read:
    list_of_values = []
    for key in keys:
        data = client.get(key)
        list_of_values.append(data)
    list_of_lists.append(list_of_values)

# Склейка с ключами
list_of_dict = []
for client in list_of_lists:
    glued_dict = dict(zip(keys, client))
    list_of_dict.append(glued_dict)

for i in range(len(list_of_books)):
    client_index = i % len(list_of_dict)
    if list_of_dict[client_index]["books"] is None:
        list_of_dict[client_index]["books"] = []
    list_of_dict[client_index]["books"].append(list_of_books[i])

with open(JSON_FILE_RESULT, "w") as f:
    json.dump(list_of_dict, f, indent=4)
