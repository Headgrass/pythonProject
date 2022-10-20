import json

BD = {'Иванов': {'adress': 'MSK center', 'email': 'asdsad@asdf.ru',
                 'phones': [64654654664, 634563456464, 33434345, 54354345345]}}


def load():
    # загрузить из json
    fname = 'BD.json'  # открываем файл
    with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
        print('БД успешно загружена')
        return BD_local


def save():
    # сохранить в json
    with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на чтение
        fh.write(json.dumps(BD, ensure_ascii=False))  # преобразовываем словарь data в unicode строку
    print('БД успешно сохранена')


# save()

BDnew = load()
print(BDnew)
