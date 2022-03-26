from HW_5_Decorators.decorator_logger import logger_constructor_decor

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]
class FlatIterator:
    def __init__(self, my_list):
        self.my_list = my_list
    def __iter__(self):
        self.count_1 = 0
        self.count_2 = -1
        return self

    @logger_constructor_decor()
    def __next__(self):
        if self.count_2 == len(self.my_list[self.count_1])-1:
            self.count_2 = -1
            self.count_1 += 1
        if self.count_1 == len(self.my_list):
            raise StopIteration
        self.count_2 += 1
        return self.my_list[self.count_1][self.count_2]
print('Итератор')

for item in FlatIterator(nested_list):
    print(item)



# print('Генератор списка')
# flat_list = [item for item in FlatIterator(nested_list)]
# print(flat_list)

# print('Генератор')
# @loger_constructor_decor('log_file.txt', None)
# def flat_generator(my_list):
#     for row in my_list:
#         if type(row) is list:
#             for element in row:
#                 yield element
#         else:
#             yield row
# for item in flat_generator(nested_list):
#     print(item)

# class FlatIterator:
#
#     def __init__(self, multi_list):
#
#         self.multi_list = multi_list  # список с вложенными списками
#
#     def __iter__(self):
#         self.multi_list_iter = iter(self.multi_list)
#         self.nested_list = []  # вложенный список с элементами
#         self.nested_list_cursor = -1
#         return self
#
#     def __next__(self):
#         self.nested_list_cursor += 1
#         print(self.nested_list)
#         if len(self.nested_list) == self.nested_list_cursor:
#             self.nested_list = None
#             self.nested_list_cursor = 0
#             print(self.nested_list)
#             while not self.nested_list:
#                 self.nested_list = next(self.multi_list_iter)
#                 #  если  список пустой, то получаем следующий
#                 #  если списки закончаться, получим stop iteration
#
#         return self.nested_list[self.nested_list_cursor]
# for item in FlatIterator(nested_list):
#     print(item)
