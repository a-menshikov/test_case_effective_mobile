from dataclasses import dataclass, field

from validators import validator_map


@dataclass
class Note():
    """Запись в телефонной книге."""

    last_name: str = field(metadata={"ru_name": "Фамилия"})
    first_name: str = field(metadata={"ru_name": "Имя"})
    patronymic: str = field(metadata={"ru_name": "Отчество"})
    organization: str = field(metadata={"ru_name": "Организация"})
    work_phone: str = field(metadata={"ru_name": "Рабочий телефон"})
    personal_phone: str = field(metadata={"ru_name": "Личный телефон"})

    @classmethod
    def empty_data_model(cls) -> dict[str, str]:
        """Получить словарь с каркасом модели."""
        fields = cls.__dataclass_fields__
        return {field.metadata["ru_name"]: '' for field in fields.values()}

    @classmethod
    def create_object_by_runame_dict(cls, rudict: dict[str, str]) -> 'Note':
        """Создать экземпляр модели по словарю
        с русскоязычными наименованиями полей."""
        note_args = {
            field.name: rudict.get(field.metadata["ru_name"], "")
            for field in cls.__dataclass_fields__.values()
        }
        return cls(**note_args)

    def as_dict(self) -> dict[str, str]:
        """Получить словарь с данными экземпляра модели."""
        fields = self.__dataclass_fields__
        return {field.metadata["ru_name"]: getattr(
            self, field.name
        ) for field in fields.values()}

    def __str__(self) -> str:
        """Строковое представление экземпляра модели."""
        return (
            f'{self.last_name} | {self.first_name} | {self.patronymic} | '
            f'{self.organization} | {self.work_phone} | '
            f'{self.personal_phone}\n'
        )

    def __setattr__(self, name, value):
        if name in validator_map:
            validator = validator_map[name]
            validator(value)
        super().__setattr__(name, value)
