from config import FUNCTIONS
from repository import PhoneBookRepository
from models import Note


class Interface():

    def __init__(self):
        self.commands: dict[str, str] = FUNCTIONS
        self.repo = PhoneBookRepository()

    def all_commands(self):
        for id, command in self.commands.items():
            print(f'{id}. {command}')
        print()

    def create_note(self):
        params = {
            'Фамилия': '',
            'Имя': '',
            'Отчество': '',
            'Организация': '',
            'Рабочий телефон': '',
            'Личный телефон': '',
        }
        for param in params:
            input_text = input(f'Заполните поле {param}: ')
            # тут будет валидация
            params[param] = input_text
        note = Note(
            last_name=params['Фамилия'],
            first_name=params['Имя'],
            patronymic=params['Отчество'],
            organization=params['Организация'],
            work_phone=params['Рабочий телефон'],
            personal_phone=params['Личный телефон'],
        )
        self.repo.write_note(note)
        print('Запись добавлена\n')

    def read_book(self):
        count_notes = self.repo.count_notes()
        if count_notes % self.repo.page_size:
            count_pages = count_notes // self.repo.page_size + 1
        else:
            count_pages = count_notes // self.repo.page_size
        print(f'\nКоличество записей: {count_notes}')
        print(f'Размер страницы: {self.repo.page_size}')
        print(f'Страниц в справочнике: {count_pages}\n')
        num_page = int(input('Введите номер страницы: '))
        print()
        if num_page > count_pages or num_page < 1:
            print('Такой страницы не существует\n')
            return
        for note in self.repo.read_page(num_page):
            print(note)

    def run(self):
        print('Телефонный справочник запущен\n')

        while True:
            print('\nДоступные команды:\n')
            self.all_commands()
            command = input('Введите id команды: ')
            if command == '0':
                print('Телефонный справочник завершает работу\n')
                break
            if command == '1':
                self.read_book()
            if command == '2':
                self.create_note()
