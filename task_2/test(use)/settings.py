TEST_FILENAME = 'test(test(use)).txt'


# methods
def write_to_file(dict):
    with open(TEST_FILENAME, 'a', encoding='utf-8') as f:
        f.write(dict+': '+'\n')


def clearing_a_file():
    with open(TEST_FILENAME,'w'):
        pass

