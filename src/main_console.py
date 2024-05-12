import requests

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8080

    print('Запросы:')
    print('1 - Получить список заметок')
    print('2 - Получить информацию о заметке')
    print('3 - Получить текст заметки')
    print('4 - Добавить новую заметку')
    print('5 - Обновить текст заметки')
    print('6 - Удалить заметку')
    act = int(input('Введите номер: '))
    token = input('Введите токен: ')

    match act:
        case 1:
            response = requests.get(f'http://{HOST}:{PORT}/get_notes', params={'token': token})
        case 2:
            id = int(input('Введите id заметки: '))
            response = requests.get(f'http://{HOST}:{PORT}/get_note_info', params={'id': id, 'token': token})
        case 3:
            id = int(input('Введите id заметки: '))
            response = requests.get(f'http://{HOST}:{PORT}/get_note_text', params={'id': id, 'token': token})
        case 4:
            text = input('Введите текст заметки: ')
            response = requests.post(f'http://{HOST}:{PORT}/create_note', params={'text': text, 'token': token})
        case 5:
            id = int(input('Введите id заметки: '))
            text = input('Введите текст заметки: ')
            response = requests.patch(f'http://{HOST}:{PORT}/update_note', params={'id': id, 'text': text, 'token': token})
        case 6:
            id = int(input('Введите id заметки: '))
            response = requests.delete(f'http://{HOST}:{PORT}/delete_note', params={'id': id, 'token': token})
    print(f'Status code: {response.status_code}')
    print(f'Response body: {response.text}')