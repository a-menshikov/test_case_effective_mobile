from dataclasses import dataclass


@dataclass
class Note():

    last_name: str
    first_name: str
    patronymic: str
    organization: str
    work_phone: str
    personal_phone: str

    def as_dict(self) -> dict[str, str]:
        return {
            'Фамилия': self.last_name,
            'Имя': self.first_name,
            'Отчество': self.patronymic,
            'Организация': self.organization,
            'Рабочий телефон': self.work_phone,
            'Личный телефон': self.personal_phone,
        }

    def __str__(self) -> str:
        return (
            f'{self.last_name} | {self.first_name} | {self.patronymic} | '
            f'{self.organization} | {self.work_phone} | '
            f'{self.personal_phone}\n'
        )
