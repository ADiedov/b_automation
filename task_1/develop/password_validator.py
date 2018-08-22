import re
import task_1.develop.settings_information_and_methods as sett


def checking_for_bad_characters(password):
    val = True
    for i in sett.UNACCEPTABLE_SYMBOLS:
        pf = password.find(i)
        if pf != -1:
           return False
    return val


def password_validator_function(password):
    match = False
    length = len(password)
    if length >= sett.MIN_LENGTH:
        if length <= sett.MAX_LENGTH:
            if re.match(sett.PATTERN, password):
                if checking_for_bad_characters(password):
                    match = True
                    sett.write_to_file(password, sett.OK)
                else:
                    match = False
                    sett.write_to_file(password, sett.NOT_OK)
            else:
                match = False
                sett.write_to_file(password, sett.NOT_OK)
        else:
            print('Password very big!')
            sett.write_to_file(password, sett.BIG)
    else:
        sett.write_to_file(password, sett.SMALL)
        print('Password is very small!')
    password = 0
    return match