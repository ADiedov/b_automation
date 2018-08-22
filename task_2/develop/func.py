import random
import string


def function(first_list_length, second_list_length):
    # initialization
    keys = [x for x in range(0, first_list_length+1)]
    values = [x for x in range(0, second_list_length+1)]

    length_keys = len(keys)
    length_values = len(values)

    if length_keys > length_values:
        while length_keys > length_values:
            values.append(None)
            length_values += 1

    if length_keys < length_values:
        values = values[:length_keys]

    target_dict = dict(zip(keys, values))
    return target_dict

