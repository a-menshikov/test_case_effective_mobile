from dataclasses import dataclass


@dataclass
class Note():
    """Запись в телефонной книге."""

    last_name: str
    first_name: str
    patronymic: str
    organization: str
    work_phone: str
    personal_phone: str

    @classmethod
    def empty_data_model(cls) -> dict[str, str]:
        """Получить словарь с каркасом модели."""
        return {
            'Фамилия': '',
            'Имя': '',
            'Отчество': '',
            'Организация': '',
            'Рабочий телефон': '',
            'Личный телефон': '',
        }

    def as_dict(self) -> dict[str, str]:
        """Получить словарь с данными экземпляра модели."""
        return {
            'Фамилия': self.last_name,
            'Имя': self.first_name,
            'Отчество': self.patronymic,
            'Организация': self.organization,
            'Рабочий телефон': self.work_phone,
            'Личный телефон': self.personal_phone,
        }

    def __str__(self) -> str:
        """Строковое представление экземпляра модели."""
        return (
            f'{self.last_name} | {self.first_name} | {self.patronymic} | '
            f'{self.organization} | {self.work_phone} | '
            f'{self.personal_phone}\n'
        )
