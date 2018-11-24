# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
# current_dir = os.path.dirname(os.path.abspath(__file__))

print('-' * 40)

def find_file(files_list = []):
    n = 0
    text = input('Введите текст для поиска:')
    if files_list == []:
        os.chdir('/Users/azarovdn/Desktop/Netology/03_Python/08_Work_whth_path/Migrations')
        for files in os.listdir("/Users/azarovdn/Desktop/Netology/03_Python/08_Work_whth_path/Migrations/"):
            file_inside = True
            if files.endswith(".sql"):
                with open(files) as file:
                    for line in file:
                        if text in line and file_inside is True:
                            files_list.append(files)
                            n += 1
                            file_inside = False

    else:
        files_list_doubler = []
        for files in files_list:
            with open(files) as file:
                file_inside = True
                for line in file:
                    if text in line and file_inside is True:
                        files_list_doubler.append(files)
                        file_inside = False
                        n += 1
        files_list = files_list_doubler

    if files_list == []:
        print('Файлы не обнаружены')
        return
    elif len(files_list) > 10:
        print('... большой список файлов ...')
        print('Всего: {}'.format(len(files_list)))
        find_file(files_list)
    elif len(files_list) > 1:
        print('Всего: {}'.format(len(files_list)))
        for file in files_list:
            print('{}/{}'.format(migrations,file))
        find_file(files_list)
    elif len(files_list) == 1:
        print('{}/{}'.format(migrations,files_list[0]))
        return


find_file()



# if __name__ == '__main__':
#     passv