import task_2.develop.func as func


def execution():
    first_list_length = int(input('Enter to N value:'))
    second_list_length = int(input('Enter to M value:'))
    target_dict = func.function(first_list_length,second_list_length)
    print(target_dict)


def main():
    execution()


if __name__ == '__main__':
    main()