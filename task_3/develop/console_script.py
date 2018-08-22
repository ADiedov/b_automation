import re
import task_3.develop.calculator as calc
import task_3.develop.settings as settings
import copy


class ConsoleScript():

    def __init__(self):
        self.calculator = calc.Calculator()
        #Variables
        self.counter_l = 0
        self.counter_r = 0
        self.save_to_memory = False
        self.operation_number = 0
        self.first_number = 0
        self.second_number = 0
        self.user_string_expression = ''
        self.substring1 = ''
        self.substring2 = ''
        self.local_s_sub_1 = False
        self.local_s_sub_2 = False
        self.first_minus = False
        self.second_minus = False

    def match(self, pattern, str):
        if re.match(pattern, str):
            return True
        else:
            return False

    #0 Очищаем состояние
    def clear_all(self):
        self.counter_l = 0
        self.counter_r = 0
        self.save_to_memory = False
        self.operation_number = 0
        self.first_number = 0
        self.second_number = 0
        self.user_string_expression = ''
        self.substring1 = ''
        self.substring2 = ''
        self.local_s_sub_1 = False
        self.local_s_sub_2 = False

    # step 0
    # Clear memory command
    # Очистить результат работы  M|(....
    def clear_memory(self):
        if self.user_string_expression == 'Clear':
            self.calculator._memory_result = None
            raise Exception('Memory clear!')

    # step 1
    # замена M-2 на D для внутреннего представления
    def delete_m_minus(self):
        count = self.user_string_expression.count('M-2')
        if count > 2:
            raise ValueError('M-2 > 2.')
        self.user_string_expression = self.user_string_expression.replace('M-2', 'D')

    # step 2
    # Получение переменных со строки ввода
    def get_numbers(self):
        try:
            data = re.findall(settings.PATTERN, self.user_string_expression)

            if data[0][0] == '':
                if data[0][1] == 'D':
                    self.first_number = self.calculator.get_data_from_memory()    # получение данных из памяти
                if data[0][1] == '-D':
                    # нуждаемся в замене на валидаторе -D -> D
                    self.user_string_expression=self.user_string_expression.replace('-D', 'D', 1)
                    self.first_number = -self.calculator.get_data_from_memory()   # получение данных из памяти
            else:
                self.first_number = int(data[0][0])
                if self.first_number < 0:
                    self.user_string_expression = self.user_string_expression.replace(data[0][0], '1')
            if data[1][0] == '':
                if data[1][1] == 'D':
                    self.second_number = self.calculator.get_data_from_memory()    # получение данных из памяти
                if data[1][1] == '-D':
                    # нуждаемся в замене на валидаторе -D -> D
                    self.user_string_expression = self.user_string_expression.replace('-D', 'D', 1)
                    self.second_number = -self.calculator.get_data_from_memory()   # получение данных из памяти
            else:
                self.second_number = int(data[1][0])
        except Exception as ex:
            print('The string does not match the format: {0}'.format(ex))

    # step 3
    def definition_of_an_operation(self):
        try:
            for i in settings.OPERATIONS_DICT.keys():          # перебор словаря со значениями операций
                part = self.user_string_expression.partition(i)
                if part[1] == i:
                    self.substring1 = part[0]
                    self.substring2 = part[2]
                    if part[1] == '-':
                        if self.second_number < 0:
                            self.second_number = -self.second_number
                    self.operation_number = settings.OPERATIONS_DICT[i]
                    self.calculator.oper_number = settings.OPERATIONS_DICT[i]

                else:
                    pass
        except Exception as ex:
            print('The string does not match the format: {0}'.format(ex))

    # step 4 Валидация строк по шаблонам
    def sub_string_validator(self):
        if self.match(settings.PATTERN_FOR_SUBSTRING_1, self.substring1):
            print('string is OK')
        else:
            raise Exception('substring 1 not format!')
        if self.match(settings.PATTERN_FOR_SUBSTRING_2, self.substring2):
            print('string is OK')
        else:
            raise Exception('substring 2 not format!')

    # step 5 Проверка на необходимость локального сохранения подстроки 1
    def check_for_saving_to_the_buffer_subst1(self):
        if self.match(settings.LOCAL_SAVE_1, self.substring1):
            self.calculator.argument_memory(self.first_number)
            print('Save local res')
        else:
            self.calculator.add_buffer(self.first_number)

    # step 6 Аналогично
    def check_for_saving_to_the_buffer_subst2(self):
        if self.match(settings.LOCAL_SAVE_2,self.substring2):
            self.calculator.argument_memory(self.second_number)
            print('Save local res')
        else:
            self.calculator.add_buffer(self.second_number)

    # step 7 Проверка на необходимость сохранения результата
    def save_all(self):
        if self.match(settings.GLOBAL_SAVE,self.substring1):
            self.calculator.save_result_to_memory()
            print('Save res')
        else:
            self.calculator._memory_result = self.calculator._memory_result
            #print('Not match')

    # Выполнение скрипта
    def exe(self):
        self.clear_memory()
    # validators
        self.delete_m_minus()
        self.get_numbers()
        self.definition_of_an_operation()
        self.sub_string_validator()
    # initialization
        self.check_for_saving_to_the_buffer_subst1()
        self.check_for_saving_to_the_buffer_subst2()
    # execution
        self.calculator.choise_of_operation()
    # results
        self.save_all()
        self.clear_all()
        return self.calculator.get_result()

    @property
    def _string(self):
        return self.user_string_expression

    @_string.setter
    def _string(self, str):
        self.user_string_expression = str





