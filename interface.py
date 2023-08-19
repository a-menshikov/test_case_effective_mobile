from config import FUNCTIONS


class Interface():

    def __init__(self):
        self.commands: dict[str, str] = FUNCTIONS

    def all_commands(self):
        for id, command in self.commands.items():
            print(f'{id}. {command}')

    def run(self):
        print('Телефонный справочник запущен\n')

        while True:
            print('Доступные команды:\n')
            self.all_commands()
            command = input('Введите id команды: ')
            if command == '0':
                break
            if command in self.commands:
                print(self.commands[command])
