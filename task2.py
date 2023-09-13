# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def my_txt(txt):
    *path_file, name = txt.split('\\')
    name_res, end_name = name.split('.')
    res_tuple = ('\\'.join(path_file), name_res, end_name)
    return res_tuple

my_string = 'C:\\Users\\Mikhail\\Desktop\\учеба\\PythonGB\\Home_Work_5\\task2.py'
print(my_txt(my_string))
