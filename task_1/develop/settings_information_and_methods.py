# settings file

# constants
PATTERN = r'^[a-zA-Z]+((?=.*[A-Z]+)(?=.*[a-z]+)(?=.*[0-9]+)' + \
           '(?=.*[!@#$%^&*-+=|:.?~]+)).{1,18}([0-9])'
MAX_LENGTH = 20
MIN_LENGTH = 6
UNACCEPTABLE_SYMBOLS = ['<', '>', '`', '(', ')', '{', '}', '/', ',', ' ', '[', ']', "'", '"', '_']

# debug info
DEBUG_AND_TEST_FILENAME = 'passwords.txt'
OK = 'OK'
NOT_OK = 'OK'
BIG = 'BIG'
SMALL = 'SMALL'


# methods
def write_to_file(password, status):
    with open(DEBUG_AND_TEST_FILENAME, 'a', encoding='utf-8') as f:
        f.write(password+': '+str(status)+'\n')


def clearing_a_file():
    with open(DEBUG_AND_TEST_FILENAME,'w'):
        pass







