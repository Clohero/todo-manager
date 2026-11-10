import todo_lib

def ask_number():
    num = input("Номер дела: ")
    try:
        return int(num) 
    except ValueError:
        print("нужно ввести число")
        return None

def menu():
    while True:
        print("1. Показать дело")
        print("2. Добавить дело")
        print("3. Удалить дело")
        print("0. Выход")
        choice = input("Выберите пункт: ")
        if choice == "1":
            todo_lib.show_todos()
        elif choice == "0":
            break
        elif choice == "2":
            text = input("Что добавить: ")
            todo_lib.add_todo(text)
        elif choice == "3":
            number = ask_number()
            if number is not None:
                todo_lib.remove_todo(number)
        else:
            print("Нет такого пункта")

menu()