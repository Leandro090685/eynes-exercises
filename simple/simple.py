import random


def simple_list():
    list_of_dicts = []

    for i in range(10):

        dict_entry = {"id": i + 1, "age": random.randint(1, 100)}
        list_of_dicts.append(dict_entry)

    return list_of_dicts


def sort_list(dicts):
    sorted_list = sorted(dicts, key=lambda x: x["age"])
    return sorted_list
