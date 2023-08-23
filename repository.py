from models import Note
import os
from itertools import islice
from config import PAGE_SIZE


class PhoneBookRepository:
    def __init__(self):
        self.file_path: str = 'phone_book.txt'
        self.current_id: int = self.count_notes() + 1
        self.page_size: int = PAGE_SIZE

    def delete_book(self):
        os.remove(self.file_path)

    def post_note(self, note: Note):
        with open(self.file_path, 'a') as file:
            file.write(str(self.current_id) + ' | ' + str(note))
        self.current_id += 1

    def count_notes(self):
        with open(self.file_path, 'r') as file:
            return len(file.readlines())

    def get_page(self, num_page: int):
        with open(self.file_path, 'r') as file:
            start = ((num_page - 1) * self.page_size)
            finish = num_page * self.page_size + 1
            sliced = islice(file, start, finish)
            page = [note for note in sliced]
            return page

    def get_note(self, id: int) -> Note:
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

    def patch_note(self, note: Note, id: int):
        with open(self.file_path, 'r') as file:
            data = file.readlines()
        data[id - 1] = str(id) + ' | ' + str(note)
        with open(self.file_path, 'w') as file:
            file.writelines(data)
