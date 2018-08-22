import random as rand
import task_2.develop.func as func
import task_2.use.settings as settings


def experiment(count):

    iteration = 0
    for iteration in range(count):
        first_list_length = rand.randint(0, 16)
        second_list_length = rand.randint(0, 16)
        data = func.function(first_list_length, second_list_length)
        settings.write_to_file(str(data))
        #iteration = iteration+1


