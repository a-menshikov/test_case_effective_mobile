from models import Note
import os
from config import PAGE_SIZE


class PhoneBookRepository:
    def __init__(self):
        self.file_path: str = 'phone_book.txt'
        self.current_id: int = self.count_notes() + 1
        self.page_size: int = PAGE_SIZE

    # def get_last_index(self):
    #     with open(self.file_path, 'r') as file:
    #         return len(file.readlines()) + 1

    def delete_book(self):
        os.remove(self.file_path)

    def write_note(self, note: Note):
        with open(self.file_path, 'a') as file:
            file.write(str(self.current_id) + ' | ' + str(note))
        self.current_id += 1

    def count_notes(self):
        with open(self.file_path, 'r') as file:
            return len(file.readlines())

    def read_page(self, num_page: int):
        with open(self.file_path, 'r') as file:
            start = ((num_page - 1) * self.page_size) + 1
            finish = num_page * self.page_size
            page = []
            for num, note in enumerate(file, 1):
                if num < start:
                    continue
                if num > finish:
                    break
                page.append(note)
            return page
