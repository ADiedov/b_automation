import task_2.use.script as sc
import task_2.use.settings as settings


def execution():
    exe = True
    while exe:
        settings.clearing_a_file()
        try:
            print('Enter number or stop:')
            count = input('Enter experiment count:')
            if count == 'stop':
                exe = False
                break
            count = int(count)
            if count>40:
                print('Very big count!')
                continue
            sc.experiment(count)
        except Exception as ex:
            print(ex)


def main():
    execution()


if __name__ == '__main__':
    main()

