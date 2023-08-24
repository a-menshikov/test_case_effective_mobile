import re


def validate_name(value: str) -> None:
    """Валидация полей полного имени."""
    if not re.match(r"^[А-Яа-яёЁ]{1,50}$", value):
        raise ValueError("Некорректное значение имени, фамилии или отчества")


def validate_organization(value: str) -> None:
    """Валидация поля организации."""
    if not re.match(r"^[А-Яа-яёЁ\s\"']{1,100}$", value):
        raise ValueError("Некорректное значение организации")


def validate_work_phone(value: str) -> None:
    """Валидация поля рабочего телефона."""
    if not re.match(r"^\d{6}$", value):
        raise ValueError("Некорректное значение рабочего телефона")


def validate_personal_phone(value: str) -> None:
    """Валидация поля личного телефона."""
    if not re.match(r"^\d{11}$", value):
        raise ValueError("Некорректное значение личного телефона")


validator_map: dict[str, callable] = {
    "last_name": validate_name,
    "first_name": validate_name,
    "patronymic": validate_name,
    "organization": validate_organization,
    "work_phone": validate_work_phone,
    "personal_phone": validate_personal_phone
}
