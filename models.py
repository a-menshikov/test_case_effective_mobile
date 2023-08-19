from dataclasses import dataclass


@dataclass
class Note():

    id: int
    last_name: str
    first_name: str
    patronymic: str
    organization: str
    work_phone: str
    personal_phone: str

    def __str__(self) -> str:
        return (
            f'{self.id} | {self.last_name} {self.first_name} {self.patronymic}'
            f' | {self.organization} | {self.work_phone}'
            f' | {self.personal_phone}\n')
