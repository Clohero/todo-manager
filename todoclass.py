import json

class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.todos = []
        self.load()

    def add(self, text):
        self.todos.append(text)
        self.save()

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.todos = json.load(f)
        except (FileNotFoundError, ValueError):
            self.todos = []

    def show(self):
        if not self.todos:
            print("Список дел пуст")
        else:
            for i, t in enumerate(self.todos, 1):
                print(f"{i}. {t}")

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)
                
    def remove(self, number):
        if number < 1:
            print("Нет такого дела")
            return None
        try:
            self.todos.pop(number - 1)
            self.save()
        except IndexError:
            print("Нет такого дела")

t = TodoList("oop_todo.json")
t.show()

# t = TodoList("oop_todo.json")
# t.add("хлеб")
# t.add("сыр")
# t.show()
# t.remove(0)
# t.remove(99)
# t.remove(1)
# t.show()