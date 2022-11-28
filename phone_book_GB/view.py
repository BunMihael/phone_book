
def menu():
    choice = 0
    while choice != 5:
        choice = int(input(menu_greeting))
        if choice == 1:
            with open('main.txt', mode='r', encoding="utf-8") as f:
                print(f'\vРанее было записано:\n {f.read()}\v')
        elif choice > 1 and choice < 5:
            return choice   
        elif choice > 5:
            print('Недопустимый пункт меню.') 


menu_greeting = '''Вас приветствует ТЕЛЕФОННЫЙ СПРАВОЧНИК!
МЕНЮ:
1. Посмотреть последнюю запись
2. Добавить новую запись
3. Импортировать в черновик
4. Экспорт в файл
5. Выход\n'''
