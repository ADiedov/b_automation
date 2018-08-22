import task_1.develop.password_validator as pv


def execution():
    while True:
        user_password = input('Enter your password: ')
        if pv.password_validator_function(user_password):
            print('Password is correct!')
            break
        else:
            print('Password is not correct!')


def main():
    execution()


if __name__ == '__main__':
    main()
