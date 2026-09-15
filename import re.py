import re
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Date:
    dd: int
    mm: int
    yyyy: int


@dataclass
class Patient:
    passport: str
    name: str
    birth_date: Date
    phone: str
    temperature: float



def read_passport():
    while True:
        input_data = input("Введите паспорт (ss ss-nnnnnn): ")

        if re.fullmatch(r"\d{2} \d{2}-\d{6}", input_data):
            return input_data

        print("Ошибка! Неверный формат паспорта.")

def read_name():
    while True:
        input_data = input("Введите имя: ")

        if input_data.strip():
            return input_data

        print("Ошибка! Имя не может быть пустым.")

def read_birth_date():
    while True:
        input_data = input("Введите дату рождения (yyyy-mm-dd): ")

        try:
            date = datetime.strptime(input_data, "%Y-%m-%d")

            return Date(
                dd=date.day,
                mm=date.month,
                yyyy=date.year
            )

        except ValueError:
            print("Ошибка! Неверная дата.")


def read_phone():
    while True:
        input_data = input("Введите телефон: ")

        valid = (
            re.fullmatch(r"\+\d\(\d{3}\) \d{3}-\d{2}-\d{2}", input_data)
            or
            re.fullmatch(r"\d\(\d{3}\) \d{3}-\d{4}", input_data)
        )

        if valid:
            return input_data

        print("Ошибка! Неверный формат телефона.")


def read_temperature():
    while True:
        input_data = input("Введите температуру (например, 36.60): ")

        try:
            return float(input_data)

        except ValueError:
            print("Ошибка! Введите корректное число.")



def main():
    print("Введите данные о пациенте")

    patient = Patient(
        passport=read_passport(),
        name=read_name(),
        birth_date=read_birth_date(),
        phone=read_phone(),
        temperature=read_temperature()
    )

    print("\nДанные пациента")
    print(f"Паспорт: {patient.passport}")
    print(f"Имя: {patient.name}")

    print(
        f"Дата рождения: "
        f"{patient.birth_date.yyyy:04d}-"
        f"{patient.birth_date.mm:02d}-"
        f"{patient.birth_date.dd:02d}"
    )

    print(f"Телефон: {patient.phone}")
    print(f"Температура: {patient.temperature:.2f}")

    print("\nВыход")
    input("Нажмите Enter для выхода...")


if __name__ == "__main__":
    main()