import task_3.develop.console_script as sc


def execution():
    exe = True
    user_expression = None
    script = sc.ConsoleScript()
    error = ''
    print('Save all with parameters: M|(M|number)operation(M|number)-save numbers to memory-buffer \n'
          + 'and save result to memory.')
    print('Save operation result to memory: M|(number)operation(number)\n')
    print('Simple calculator: (number)operaion(number) or number operation number')
    print(
        'Use memory: M| (M-2)operation (number);number operation(M-2) or (M-2)oper(M-2).\n'
        'Attention!If memory-result was not to be saved, you get error!')
    print('M - save to memory buffer.Without M - number will save to simple buffer')
    print('command:Clear - cleared memory')

    while exe:
        print(error)
        error = ''
        try:
            user_expression = input('Enter your expression')
            script._string = user_expression
            res = script.exe()
            print('Result:')
            print(res)
        except Exception as ex:
            error = ex
        finally:
            print('Next expression:')


def main():
    execution()


if __name__ == '__main__':
    main()