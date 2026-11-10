import json

def load_todos(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        return loaded
    except (FileNotFoundError, ValueError):
        return []

def save_todos(todos, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def add_todo(text):
    todos = load_todos("todo.json")
    todos.append(text)
    save_todos(todos, "todo.json")

def show_todos():
    todos = load_todos("todo.json")
    if not todos:
        print("список дел пуст")
    else:
        for i, t in enumerate(todos, 1):
            print(f"{i}. {t}")

def remove_todo(number):
    if number < 1:
        print("некорректное значение")
        return
    todos = load_todos("todo.json")
    try:
        todos.pop(number - 1)
        save_todos(todos, "todo.json")
    except IndexError:
        print("нет такого дела")

