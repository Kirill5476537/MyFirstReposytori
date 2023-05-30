
class Todo:

    menu = {'1': 'Добавить дело', '2': 'Список всех дел', '3': 'Найти дело',
                '4': 'Выполнить дело', '5': 'Повторить дело', '6': 'Выйти'}

    def __init__(self):
        self.todo_items = [] #Список дел.

    def add_todo(self, items):
        self.todo_items.append(items)
        print("Задача успешно добавлена")

    def list(self):
        print("Список дел:")
        for item in self.todo_items:
            print(str(item.counter) + '.' + item.name + '(Выполнено)' * int(item.is_done))
        print()

    def find(self):
        pass

    def run(self):

       while True:

           # Заголовок программы.
           print('Меню:')

           # Вывод меню на экран.
           # Перебираем словрь, и выводим ключ и значение.
           for key, val in Todo.menu.items():
                print(key + '.' + val, end='\n')

           # Спросить у пользователя какую команду выполнить.
           command = input('Введите номер команды: ')

           # Обработка выбора команды.
           if command == '1':
               #Добавляем новое дело
               name_ToDo = input("Какое дело?") # запрашиваем у пользователя имя нового дела
               new_ToDo = TodoItem(name_ToDo)   # создаем элемент класса TodoItem (задачу)

               self.add_todo(new_ToDo)  # Поместить задачу в список.

           elif command == '2':
               # Показываем список дел
               self.list()

           elif command == '3':
               # Найдем дело
            pass
           elif command == '4':
               # Выполнить дело
            pass
           elif command == '5':
               # Повторииь дело
            pass
           elif command == '6':
               # Выход из программы
               print("Программа завершена.")
               break

class TodoItem:

    counter_do = 0

    def __init__(self, new_do):
        self.is_done = False
        self.name = new_do

        TodoItem.counter_do += 1
        self.counter = TodoItem.counter_do

    def check(self):
        self.is_done = True

    def uncheck(self):
        self.is_done = False

#if name == 'main':
todo = Todo()
todo.run()

