from itertools import islice

from config import FILE_PATH, PAGE_SIZE
from models import Note


class PhoneBookRepository:
    """Репозиторий телефонной книги."""

    def __init__(self) -> None:
        self.file_path: str = FILE_PATH
        self.current_id: int = self.count_notes() + 1
        self.page_size: int = PAGE_SIZE

    def post_note(self, note: Note) -> None:
        """Добавление записи."""
        with open(self.file_path, 'a') as file:
            file.write(str(self.current_id) + ' | ' + str(note))
        self.current_id += 1

    def count_notes(self) -> int:
        """Получить количество записей в файле."""
        with open(self.file_path, 'r') as file:
            return len(file.readlines())

    def get_page(self, num_page: int) -> list[str]:
        """Получить страницу записей из файла."""
        with open(self.file_path, 'r') as file:
            start = ((num_page - 1) * self.page_size)
            finish = num_page * self.page_size + 1
            sliced = islice(file, start, finish)
            page = [note for note in sliced]
            return page

    def get_note(self, id: int) -> Note:
        """Получить запись по id."""
        with open(self.file_path, 'r') as file:
            sliced = islice(file, id - 1, id)
            note = [note.strip().split(' | ') for note in sliced][0]
            object = Note(
                last_name=note[1],
                first_name=note[2],
                patronymic=note[3],
                organization=note[4],
                work_phone=note[5],
                personal_phone=note[6],
            )
            return object

    def patch_note(self, updated_note: Note, id: int) -> None:
        """Изменить запись по id."""
        with open(self.file_path, 'r') as file:
            data = file.readlines()
        data[id - 1] = str(id) + ' | ' + str(updated_note)
        with open(self.file_path, 'w') as file:
            file.writelines(data)

    def search_note(self, query: list[str]) -> list[str]:
        """Поиск записей."""
        with open(self.file_path, 'r') as file:
            data = file.readlines()
            result = []
            for line in data:
                note = line.strip()
                if all(
                    query[i] in note.split(' | ') for i in range(len(query))
                ):
                    result.append(note)
            return result
