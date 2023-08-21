import os

# Формат файла данных (CSV)
DATA_FILE = "phonebook.csv"

# Проверка существования файла данных и его создание, если не существует
if not os.path.isfile(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        file.write("Фамилия,Имя,Отчество,Организация,Телефон рабочий,Телефон личный\n")

def load_data():
    """
    Загрузка данных из файла.
    """
    with open(DATA_FILE, "r") as file:
        lines = file.readlines()
        if len(lines) > 1:
            return [line.strip().split(",") for line in lines[1:]]
    return []

def save_data(data):
    """
    Сохранение данных в файл.
    """
    with open(DATA_FILE, "w") as file:
        file.write("Фамилия,Имя,Отчество,Организация,Телефон рабочий,Телефон личный\n")
        for record in data:
            file.write(",".join(record) + "\n")

def display_records(records, page_size=10):
    """
    Вывод записей постранично.
    """
    total_records = len(records)
    if total_records == 0:
        print("Справочник пуст.")
        return

    page = 1
    while True:
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        current_page = records[start_idx:end_idx]

        print(f"Страница {page} из {((total_records - 1) // page_size) + 1}:\n")
        for record in current_page:
            print(", ".join(record))
        print()

        choice = input("Нажмите 'n' для следующей страницы, 'p' для предыдущей, 'q' для выхода: ").lower()

        if choice == 'n':
            if end_idx < total_records:
                page += 1
            else:
                print("Вы достигли конца справочника.")
        elif choice == 'p':
            if page > 1:
                page -= 1
            else:
                print("Вы на первой странице.")
        elif choice == 'q':
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

def add_record():
    """
    Добавление новой записи.
    """
    record = []
    print("Введите данные для новой записи:")
    record.append(input("Фамилия: "))
    record.append(input("Имя: "))
    record.append(input("Отчество: "))
    record.append(input("Организация: "))
    record.append(input("Телефон рабочий: "))
    record.append(input("Телефон личный: "))

    records = load_data()
    records.append(record)
    save_data(records)
    print("Запись успешно добавлена.")

def edit_record():
    """
    Редактирование существующей записи.
    """
    records = load_data()
    if not records:
        print("Справочник пуст.")
        return

    search_term = input("Введите фамилию или имя для поиска записи: ").lower()
    matching_records = []

    for record in records:
        if search_term in record[0].lower() or search_term in record[1].lower():
            matching_records.append(record)

    if not matching_records:
        print("Запись не найдена.")
        return

    display_records(matching_records)
    selection = int(input("Выберите номер записи для редактирования: ")) - 1

    if 0 <= selection < len(matching_records):
        print(f"Редактирование записи:\n{', '.join(matching_records[selection])}")
        new_data = []
        new_data.append(input("Фамилия (оставьте пустым для сохранения текущего значения): ") or matching_records[selection][0])
        new_data.append(input("Имя (оставьте пустым для сохранения текущего значения): ") or matching_records[selection][1])
        new_data.append(input("Отчество (оставьте пустым для сохранения текущего значения): ") or matching_records[selection][2])
        new_data.append(input("Организация (оставьте пустым для сохранения текущего значения): ") or matching_records[selection][3])
        new_data.append(input("Телефон рабочий (оставьте пустым для сохранения текущего значения): ") or matching_records[selection][4])
        new_data.append(input("Телефон личный (оставьте пустым для сохранения текущего значения): ") or matching_records[selection][5])

        records[records.index(matching_records[selection])] = new_data
        save_data(records)
        print("Запись успешно отредактирована.")
    else:
        print("Некорректный выбор.")

def search_records():
    """
    Поиск записей по одной или нескольким характеристикам.
    """
    records = load_data()
    if not records:
        print("Справочник пуст.")
        return

    search_term = input("Введите ключевое слово для поиска: ").lower()
    matching_records = []

    for record in records:
        if any(search_term in field.lower() for field in record):
            matching_records.append(record)

    if not matching_records:
        print("Записи не найдены.")
        return

    display_records(matching_records)

def main():
    while True:
        print("Телефонный справочник")
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            records = load_data()
            display_records(records)
        elif choice == '2':
            add_record()
        elif choice == '3':
            edit_record()
        elif choice == '4':
            search_records()
        elif choice == '5':
            print("Завершение работы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
