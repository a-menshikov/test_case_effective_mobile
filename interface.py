from models import Note
from repository import PhoneBookRepository


class Interface():
    """Клиентский интерфейс."""

    def __init__(self) -> None:
        self.commands: dict[str, str] = {
            '1': 'Вывести справочник',
            '2': 'Добавить запись',
            '3': 'Редактировать запись',
            '4': 'Найти запись',
            '0': 'Выход',
        }
        self.methods: dict[str, callable] = {
            '1': self.read_page,
            '2': self.create_note,
            '3': self.edit_note,
            '4': self.search_note,
            '0': self.stop,
        }
        self.repo: PhoneBookRepository = PhoneBookRepository()

    def all_commands(self) -> None:
        """Вывести список доступных команд."""
        for id, command in self.commands.items():
            print(f'{id}. {command}')
        print()

    def create_note(self):
        """Добавить запись."""
        params = Note.empty_data_model()
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
        num_page = int(input('Введите номер страницы: '))
        print()
        if num_page > count_pages or num_page < 1:
            print('Такой страницы не существует\n')
            return
        for note in self.repo.get_page(num_page):
            print(note)

    def edit_note(self) -> None:
        """Редактировать запись."""
        num = int(input('\nВведите номер записи для редактирования: '))
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
        print('\nЗапись изменена')

    def search_note(self) -> None:
        """Поиск записи."""
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

    def command_router(self, command_key: str) -> None:
        """Обработка id команды."""
        command = self.methods[command_key]
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
