def new_entry():
    while True:
        try:
            with open('main.txt', 'a+', encoding='utf-8') as file:
                data = input(
                    'Введите: "Фамилия, Имя, Телефон, Описание", через запятую.\n')
                csv = file.write(f'\n{data}')
                return csv
        except:
            print('Ощибка чтения файла.')


def export_entry():
    while True:
        open_file = input(
            "Введите название файла для экспорта(для выхода нажмите 5):\n ")
        if open_file == 5:
            break
        try:
            with open(open_file, 'r', encoding='utf-8') as file:
                export_to = input(
                    "\n Введите название файла в который нужено экспортировать:\n ")
                with open(export_to, 'a+', encoding='utf-8') as file2:
                    csv = file.read()
                    export_result = file2.write(f'\n{csv}')
                return export_result
        except:
            print('Такого файла нет')


def buffer():
    with open('main.txt', 'r', encoding='utf-8') as file, open('buffer.txt', 'w', encoding='utf-8') as entry:
        data = file.read()
        buffer = entry.write(data)
        return buffer
