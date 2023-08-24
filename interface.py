from config import COMMANDS
from models import Note
from repository import PhoneBookRepository


class Interface():
    """Клиентский интерфейс."""

    def __init__(self) -> None:
        self.commands = COMMANDS
        self.repo: PhoneBookRepository = PhoneBookRepository()

    def all_commands(self) -> None:
        """Вывести список доступных команд."""
        for id, command in self.commands.items():
            print(f'{id}. {command[1]}')
        print()

    def create_note(self):
        """Добавить запись."""
        params = Note.empty_data_model()
        print()
        for param in params:
            input_text = input(f'Заполните поле {param}: ')
            params[param] = input_text
        try:
            note = Note.create_object_by_runame_dict(params)
        except ValueError as e:
            print()
            print(e)
            return
        self.repo.post_note(note)
        print('Запись добавлена\n')

    def read_page(self) -> None:
        """Вывести страницу справочника."""
        count_notes = self.repo.count_notes()
        if count_notes % self.repo.page_size:
            count_pages = count_notes // self.repo.page_size + 1
        else:
            count_pages = count_notes // self.repo.page_size
        print(f'\nКоличество записей: {count_notes}')
        print(f'Размер страницы: {self.repo.page_size}')
        print(f'Страниц в справочнике: {count_pages}\n')
        num_page = input('Введите номер страницы: ')
        print()
        try:
            num_page = int(num_page)
        except ValueError:
            print('Некорректный формат номера страницы. Только целое число\n')
            return
        if num_page > count_pages or num_page < 1:
            print('Такой страницы не существует\n')
            return
        for note in self.repo.get_page(num_page):
            print(note)

    def edit_note(self) -> None:
        """Редактировать запись."""
        num = input('\nВведите номер записи для редактирования: ')
        print()
        try:
            num = int(num)
        except ValueError:
            print('Некорректный формат id записи. Только целое число\n')
            return
        try:
            note = self.repo.get_note(num)
        except ValueError as e:
            print(e)
            return
        new_params = {}
        for key, value in note.as_dict().items():
            print(f'\nЗначение поля {key} сейчас: {value}')
            input_text = input(
                'Введите новое значение или оставьте пустым, чтобы пропустить:'
            )
            if input_text == '':
                new_params[key] = value
            else:
                new_params[key] = input_text
        try:
            new_note = Note.create_object_by_runame_dict(new_params)
        except ValueError as e:
            print()
            print(e)
            return
        self.repo.patch_note(new_note, num)
        print('\nЗапись изменена')

    def search_note(self) -> None:
        """Поиск записи."""
        print('\nВвод параметров для поиска')
        print(
            'Если параметров несколько, вводите через знак ";" без пробелов'
        )
        params = input('\nВведите строку: ').split(';')
        print()
        try:
            search_result = self.repo.search_note(params)
        except ValueError as e:
            print(e)
            return
        if len(search_result) == 0:
            print('Ничего не нашлось\n')
            return
        for note in search_result:
            print(note)

    def command_router(self, command_key: str) -> None:
        """Обработка id команды."""
        command = getattr(self, self.commands[command_key][0])
        command()

    def stop(self) -> None:
        """Завершить работу."""
        print('\nТелефонный справочник завершает работу')
        exit()

    def run(self) -> None:
        """Запустить клиентский интерфейс."""
        print('Телефонный справочник запущен\n')

        while True:
            print('\nДоступные команды:\n')
            self.all_commands()
            command = input('Введите id команды: ')
            if command not in self.commands:
                print('\nТакой команды не существует')
                continue
            self.command_router(command)
