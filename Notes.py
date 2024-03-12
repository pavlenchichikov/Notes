import json
import os
import csv
from datetime import datetime
class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump([note.__dict__ for note in notes], file)

def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as file:
            data = json.load(file)
            return [Note(**note_data) for note_data in data]
    return []

def add_note(notes, id, title, body):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append(Note(id, title, body, current_time))

def edit_note(notes, id, title, body):
    for note in notes:
        if note.id == id:
            note.title = title
            note.body = body
            break

def delete_note(notes, id):
    notes[:] = [note for note in notes if note.id != id]

def search_notes(notes, query):
    found_notes = []
    for note in notes:
        if query in note.title or query in note.body:
            found_notes.append(note)
    return found_notes

def sort_notes_by_date(notes):
    return sorted(notes, key=lambda x: x.timestamp)

def sort_notes_by_title(notes):
    return sorted(notes, key=lambda x: x.title)

def export_notes_to_csv(notes):
    with open('notes.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ID', 'Title', 'Body', 'Timestamp'])
        for note in notes:
            writer.writerow([note.id, note.title, note.body, note.timestamp])

def display_note_by_id(notes, id):
    for note in notes:
        if note.id == id:
            print(f"ID: {note.id}, Заголовок: {note.title}")
            print(f"Тело заметки: {note.body}")
            print(f"Дата/время создания: {note.timestamp}")
            return
    print("Заметка с указанным ID не найдена.")


def main():
    notes = load_notes()

    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть все заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Поиск заметок")
        print("6. Сортировка заметок")
        print("7. Экспорт заметок в CSV")
        print("8. Показать заметку по ID")
        print("9. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            if not notes:
                print("Нет сохраненных заметок.")
            else:
                for note in notes:
                    print(f"ID: {note.id}, Заголовок: {note.title}")
                    print(f"Тело заметки: {note.body}")
                    print(f"Дата/время создания: {note.timestamp}")
        elif choice == '2':
            id = input("Введите ID новой заметки: ")
            title = input("Введите заголовок: ")
            body = input("Введите текст заметки: ")
            add_note(notes, id, title, body)
            save_notes(notes)
            print("Заметка успешно добавлена.")
        elif choice == '3':
            id = input("Введите ID заметки для редактирования: ")
            title = input("Введите новый заголовок: ")
            body = input("Введите новый текст заметки: ")
            edit_note(notes, id, title, body)
            save_notes(notes)
            print("Заметка успешно отредактирована.")
        elif choice == '4':
            id = input("Введите ID заметки для удаления: ")
            delete_note(notes, id)
            save_notes(notes)
            print("Заметка успешно удалена.")
        elif choice == '5':
            query = input("Введите текст для поиска: ")
            found_notes = search_notes(notes, query)
            if found_notes:
                for note in found_notes:
                    print(f"ID: {note.id}, Заголовок: {note.title}")
                    print(f"Тело заметки: {note.body}")
                    print(f"Дата/время создания: {note.timestamp}")
            else:
                print("Заметки по вашему запросу не найдены.")
        elif choice == '6':
            sort_choice = input("Выберите способ сортировки (1 - по дате, 2 - по заголовку): ")
            if sort_choice == '1':
                sorted_notes = sort_notes_by_date(notes)
            elif sort_choice == '2':
                sorted_notes = sort_notes_by_title(notes)
            else:
                print("Некорректный ввод.")
                continue

            for note in sorted_notes:
                print(f"ID: {note.id}, Заголовок: {note.title}")
                print(f"Тело заметки: {note.body}")
                print(f"Дата/время создания: {note.timestamp}")
        elif choice == '7':
            export_notes_to_csv(notes)
            print("Заметки успешно экспортированы в CSV.")
        elif choice == '8':
            id = input("Введите ID заметки для отображения: ")
            display_note_by_id(notes, id)
        elif choice == '9':
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()