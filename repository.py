from models import Note
import os
from config import PAGE_SIZE


class PhoneBookRepository:
    def __init__(self):
        self.file_path: str = 'phone_book.txt'
        # последний айдишник как то хранить
        self.current_id: int = 1
        self.page_size: int = PAGE_SIZE

    def delete_book(self):
        os.remove(self.file_path)

    def write_note(self, note: Note):
        with open(self.file_path, 'a') as file:
            file.write(str(self.current_id) + ' | ' + str(note))
        self.current_id += 1

    def count_notes(self):
        with open(self.file_path, 'r') as file:
            line_count = len(file.readlines())
        return line_count
