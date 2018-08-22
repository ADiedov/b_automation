import math
import copy


class Calculator:

    def __init__(self):
        self._memory_buffer = []    # with local save choise_of_operation for arguments (M|arg)
        self.memory_buffer_count = 0
        self._buffer = []           # without local save choise_of_operation arg
        self.buffer_count = 0
        self._memory_result = None # saved memory var
        self._result = 0
        self.flag_1 = False        # order of operations
        self.flag_2 = False
        self.oper_number = 0       # number operations



    # for simple numbers, example 32+32 or (M|32) + 33<-(!)
    #добавление данных в буфер
    def add_buffer(self,arg):
        self._buffer.append(arg)
        self.buffer_count+=1
        if (self.flag_1 == self.flag_2) and self.flag_1 == False:
            self.flag_1 = True

    def clear_buffer(self):
        self._buffer.clear()
    # добавление данных в буфер памяти

    def argument_memory(self,arg):
        self._memory_buffer.append(arg)
        self.memory_buffer_count += 1
        if (self.flag_1 == self.flag_2) and self.flag_2 ==False:
            self.flag_2=True

    def clear_memory_buffer(self):
        self._memory_buffer.clear()

    def get_result(self):
        res = self._result
        return res

    # Если память не пуста
    def memory_not_none(self):
        if self._memory_result !=None:
            return True
        else:
            return False

    # get data from memory (М-2)
    def get_data_from_memory(self):
        if self.memory_not_none():
            return self._memory_result
        else:
            raise Exception('Not data in memory!Save your expression')

    # global M.Save all
    def save_result_to_memory(self):
        self._memory_result = 0
        self._memory_result = self.get_result()
        print('Result in memory!')

    # get data from buffer and buffer- memory
    def get_data_from_buffers(self):
        data=[]
        if self.flag_1:
            if self.buffer_count == 2:
                 data = copy.deepcopy(self._buffer)
            else:
                data.append(self._buffer[0])
                if self.memory_buffer_count==1:
                    data.append(self._memory_buffer[0])
                else:
                    raise Exception('Error data')
        if self.flag_2:
             if self.memory_buffer_count == 2:
                data = copy.deepcopy(self._memory_buffer)
             else:
                  data.append(self._memory_buffer[0])
                  if self.buffer_count==1:
                    data.append(self._buffer[0])
                  else:
                     raise Exception('Error data')

        self.all_clear()
        print(data)
        dat = data
        data = []
        return dat

    def all_clear(self):
        self.clear_memory_buffer()
        self.clear_buffer()
        self.memory_buffer_count = 0
        self.buffer_count = 0
        self.flag_1 = False
        self.flag_2 = False
    #

    def choise_of_operation(self):
        num = self.get_data_from_buffers()
        nums = self.oper_number

        if nums == 1:
            self.summ(num[0], num[1])
        if nums == 2:
            self.difference(num[0], num[1])
        if nums == 3:
            self.multiplication(num[0], num[1])
        if nums == 4:
            self.division(num[0], num[1])
        if nums == 5:
            self.sqrt(num[0], num[1])
        if nums == 6:
            self.division_without_residue(num[0], num[1])
        if nums == 7:
            self.pow(num[0], num[1])
        num = []
        self.all_clear()

    def summ(self, first=0, second=0):
        self._result = first+second

    def difference(self, first=0, second=0):
        self._result = first - second

    def multiplication(self, first=0, second=0):
        self._result = first * second

    def division(self, first=0, second=1):
        self._result = first / second

    def division_without_residue(self, first=0, second=1):
        self._result = first // second

    def pow(self, first=0, second=0):
        self._result = first ** second

    def sqrt(self, first=0, second=1):
        self._result = math.sqrt(first)+math.sqrt(second)










