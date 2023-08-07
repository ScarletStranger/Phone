def action(notes):
    while True:
        user_choice = input('1 - Импортировать заметки\n2 - Найти заметку\n3 - Добавить заметку\n4 - Изменить заметку\n5 - Удалить заметку\n6 - Все заметки\n0 - Выход\n')
        print()
        if user_choice == '1':
            add_file = input ('Введите название заметки: ')
            import_data(add_file, notes)
        elif user_choice == '2':
            note_list = read_file_to_dict(notes)
            find_note(note_list)
        elif user_choice == '3':
            add_note(notes)
        elif user_choice == '4':
            change_note(notes)
        elif user_choice == '5':
            delete_note(notes)
        elif user_choice == '6':
            show_notes(notes)
        elif user_choice == '0':
            print('Заверешние работы')
            break
        else:
            print('Неверный ввод')
            print()
            continue

def import_data(add_file,notes):
    try:
        with open(add_file, 'r', encoding='utf-8') as read_note, open(notes, 'a', encoding='utf-8') as file:
            add_note = read_note.readlines()
            file.writelines(add_note)
    except FileNotFoundError:
        print(f'{add_file} не найден')

def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Текст заметки']
    note_list = []
    for line in lines:
        line = line.strip().split()
        note_list.append(dict(zip(headers,line)))
    return note_list

def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        note_list = []
        for line in file.readlines():
            note_list.append(line.split())
    return note_list

def search_parameters():
    print('Введите текст заметки для поиска')
    search_field = input('1 - по тексту заметки')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите текст заметки для поиска: ')
        print()
    return search_field, search_value

def find_note(note_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Текст'}
    found_notes = []
    for note in note_list:
        if note[search_value_dict[search_field] == search_value]:
            found_notes.append(note)
    if len(found_notes) == 0:
        print('Заметка не найдена')
    else:
        print_notes(found_notes)
    print()

def get_new_note():
    new_note = input('Введите текст заметки: ')
    return new_note

def add_note(file_name):
    info = ' '.join(get_new_note())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')

def show_notes(file_name):
    list_of_notes = sorted(read_file_to_dict(file_name), key=lambda x: x['Текст заметки'])
    print_notes(list_of_notes)
    print()
    return list_of_notes

def search_to_modify(note_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for note in note_list:
        if note[int(search_field) - 1] == search_value:
            search_result.append(note)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько заметок')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер заметки, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Заметка не найдена')
    print()

def change_note(file_name):
    note_list = read_file_to_list(file_name)
    note_to_change = search_to_modify(note_list)
    note_list.remove(note_to_change)
    print('Введите текст заметки, которую вы хотите изменить')
    field = input('1 - текст заметки')
    if field == '1':
        note_to_change[0] = input('Введите текст заметки: ')
    note_list.append(note_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in note_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_note(file_name):
    note_list = read_file_to_list(file_name)
    note_to_change = search_to_modify(note_list)
    note_list.remove(note_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for note in note_list:
            line = ' '.join(note) + '\n'
            file.write(line)


def print_notes(note_list: list):
    for note in note_list:
        for key, value in note.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'notes.txt'
    action(file)