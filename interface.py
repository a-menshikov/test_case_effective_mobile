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
        self.repo.post_note(note)
        print('Запись добавлена\n')

    def read_page(self):
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
        for note in self.repo.get_page(num_page):
            print(note)

    def edit_note(self):
        num = int(input('Введите номер записи для редактирования: '))
        note = self.repo.get_note(num)
        new_params = {}
        for key, value in note.as_dict().items():
            print(f'\nЗначение поля {key} сейчас: {value}')
            input_text = input(
                'Введите новое значение или оставьте пустым, чтобы пропустить:'
            )
            if input_text == '':
                new_params[key] = value
            else:
                # тут будет валидация
                new_params[key] = input_text
        new_note = Note(
            last_name=new_params['Фамилия'],
            first_name=new_params['Имя'],
            patronymic=new_params['Отчество'],
            organization=new_params['Организация'],
            work_phone=new_params['Рабочий телефон'],
            personal_phone=new_params['Личный телефон'],
        )
        self.repo.patch_note(new_note, num)
        print('Запись изменена\n')

    def search_note(self):
        print('Ввод параметров для поиска')
        print(
            'Если параметров несколько, вводите через знак ";" без пробелов'
        )
        params = input('\nВведите строку: ').split(';')
        print()
        search_result = self.repo.search_note(params)
        if len(search_result) == 0:
            print('Ничего не нашлось\n')
            return
        for note in search_result:
            print(note)

    def stop(self):
        print('Телефонный справочник завершает работу\n')

    def run(self):
        print('Телефонный справочник запущен\n')

        while True:
            print('\nДоступные команды:\n')
            self.all_commands()
            command = input('Введите id команды: ')
            if command == '0':
                self.stop()
                break
            if command == '1':
                self.read_page()
            if command == '2':
                self.create_note()
            if command == '3':
                self.edit_note()
            if command == '4':
                self.search_note()
