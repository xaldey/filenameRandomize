import os
import random

print("Текущая папка:", os.getcwd())
current_dir = os.getcwd()
# Создадим папку для смешанных файлов (проверим отсутствие существующей)
# new_dir = current_dir
#     if not os.path.isdir("new-mp3"):
#         os.mkdir("new-mp3")

# переименовать text.txt на renamed-text.txt
# os.rename("text.txt", "renamed-text.txt")
# -------------------
# создать новый текстовый файл
# text_file = open("text.txt", "w")
# # запить текста в этот файл
# text_file.write("Это текстовый файл")
# -------------------------------
# распечатать все файлы и папки в текущем каталоге
# print("Все папки и файлы:", os.listdir())
# ------------------------
# вывести некоторые данные о файле
# print(os.stat("text.txt"))

# type_of_file: str = input("Укажи тип файлов для смешивания: ")
type_of_file = 'mp3'

# Просканировать dir_to_randomize на предмет type_of_file
# На выходе надо получить список файлов type_of_file - №1
def find_all_mp3():
    os.chdir(type_of_file)
    dir_to_rand = os.getcwd()
    print("Dir with mp3`s:", dir_to_rand)
    print("Все файлы:", os.listdir(dir_to_rand))
    list_of_files = os.listdir(dir_to_rand)
    file_list_len = int(len(list_of_files))
    print("Длина списка:", file_list_len)
    sorted(list_of_files)
    for el in list_of_files:
        print(el)
    print("-----------")
    random.shuffle(list_of_files)
    for el in list_of_files:
        print(el)
        add_hint = random.randint(1, 100)
        print(add_hint)
        # os.rename(el.title(), str(add_hint) + " - " + el.title())
        os.rename(el, str(add_hint) + " - " + el)
        print(el)
    print(list_of_files)
#     Rename files in list



# Сделать перемешивание списка
# получить список - №2
def randomize_list():
    random.shuffle(list_of_files)
    for el in list_of_files:
        print(el)
    print(list_of_files)



# Считаем длину полученного списка и создаем список рэндом-номеров такой длины
# Именно элементы этого списка мы подставим в наименование файла из первого списка
def make_helplist():
    a = []
    for i in range(1, help_list):
        a.append(i)
    print(a)



# Необходимо сменить дату создания, правки и последнего обращения к файлу
# Смена аттрибутов файлов в папке
def make_one_date():
    pass


# Переименование элементов из первого списка
# Добавляем им числа из второго списка (добавим еще префикс "-")
# Поскольку первый список уже перемешан, то добавляем по порядку
def rename_files():
    pass


def main():
    find_all_mp3()
    # randomize_list()
    # make_helplist()


if __name__ == '__main__':
    main()






