from datetime import datetime
import os

def logger_constructor_decor(file_path=None):
    if file_path is not None:
        if not os.path.exists(file_path):
            file_place = os.path.join(os.path.normpath(file_path))  # нормализуем путь
        else:
            file_place = file_path

    else:
        file_place = os.path.join(os.getcwd())
    file_path = os.path.join(file_place, 'logger_file.txt')


    def logger_decorator(old_function):

        def addition_def(*args, **kwargs):
            log_date = datetime.now()
            func_name = old_function.__name__
            input_data = f'вводные данные:{args} и {kwargs}'
            output_data = old_function(*args, **kwargs)
            result_line = f'вызвана функция {func_name} \n'\
                          f'дата и время вызова : {log_date} \n'\
                          f'{input_data} \n'\
                          f'результирующее значение функции {func_name}: {output_data}\n'\
                          f'***********\n'

            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(result_line)

            return output_data

        return addition_def

    return logger_decorator

# @logger_constructor_decor()
# def foo(a,b):
#     return a+b
#
# foo(2,3)

