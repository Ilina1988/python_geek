# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
#
# my_f = open('test.txt', 'w')
# line = input('Введите текст \n')
# while line:
#     my_f.writelines(line)
#     line = input('Введите текст \n')
#     if not line:
#         break
#
# my_f.close()
# my_f = open('test.txt', 'r')
# content = my_f.readlines()
# print(content)
# my_f.close()

# 2: Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке
# my_list = ['Name\n', 'Surname\n', 'Fathername\n']
# with open("test_2.txt", 'w+') as file_obj:
#     file_obj.writelines(my_list)
# with open("test_2.txt") as file_obj:
#     lines = 0
#     letters = 0
#     for line in file_obj:
#         lines += line.count("\n")
#         letters = len(line)-1
#         print(f"{letters} letters in line")
#     print(f"String count is {lines}")

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# def summary():
#     try:
#         with open('file_5.txt', 'w+') as file_obj:
#             line = input('Enter numbers separated by a space \n')
#             file_obj.writelines(line)
#             my_numb = line.split()
#
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Error')
#     except ValueError:
#         print('Wrong number')
# summary()