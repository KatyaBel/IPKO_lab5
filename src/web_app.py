import datetime
from fastapi import FastAPI
import model

app = FastAPI()

list_notes = []
id_notes = []

def isCorrectToken(token: str):
    f = open('files/tokens.txt', 'r')
    first_char = f.read(1)
    if first_char:
        tokens = []
        f.seek(0)
        for line in f:
            tokens.append(line[:-1])
        if token in tokens:
            return True
        else:
            return False
    else:
        return True

def add_to_list_notes():
    #очищение list_notes и id_notes
    list_notes.clear()
    id_notes.clear()
    #заполнение list_notes
    f = open('files/notes.txt', 'r')
    first_char = f.read(1)
    if first_char:
        f.seek(0)
        for line in f:
            noteMas = line.split(';')
            note = {'id': int(noteMas[0]), 'created_at': noteMas[1], 'updated_at': noteMas[2], 'text': noteMas[3]}
            list_notes.append(note)
            id_notes.append(int(noteMas[0]))
    f.close()


def write_to_file(my_list: list):
    #запись списка в файл
    f = open('files/notes.txt', 'w')
    for i in range(len(my_list)):
        f.write(str(my_list[i]['id']) + ';' + str(my_list[i]['created_at']) + ';' + str(my_list[i]['updated_at']) + ';' + my_list[i]['text'])
    f.close()


@app.get('/get_notes')
def get_notes(token: str):
    #проверка токена
    if isCorrectToken(token):
        #заполнение list_notes
        add_to_list_notes()
        note = {}
        for i in range(len(id_notes)):
            note[i] = str(id_notes[i])
        return model.GetNotes(
            notes=note
        )
    else:
        return 'Неверный токен'


@app.get('/get_note_info')
def get_note_info(id: int, token: str):
    #проверка токена
    if isCorrectToken(token):
        #заполнение list_notes
        add_to_list_notes()
        #поиск id
        if id not in id_notes:
            return 'Заметка с таким id не найдена'
        else:
            for i in range(len(id_notes)):
                if id == id_notes[i]:
                    return model.GetNoteInfo(
                        created_at=list_notes[i]['created_at'],
                        updated_at=list_notes[i]['updated_at']
                    )
    else:
        return 'Неверный токен'


@app.get('/get_note_text')
def get_note_text(id: int, token: str):
    #проверка токена
    if isCorrectToken(token):
        #заполнение list_notes
        add_to_list_notes()
        #поиск id
        if id not in id_notes:
            return 'Заметка с таким id не найдена'
        else:
            for i in range(len(id_notes)):
                if id == id_notes[i]:
                    return model.GetNoteText(
                        id=id,
                        text=list_notes[i]['text'][:-1]
                    )
    else:
        return 'Неверный токен'


@app.post('/create_note')
def create_note(text: str, token: str):
    #проверка токена
    if isCorrectToken(token):
        #заполнение list_notes
        add_to_list_notes()
        #поиск id
        id = 1
        for i in range(len(id_notes)):
            if id in id_notes:
                id += 1
        #создание дат
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        #запись в файл
        f = open('files/notes.txt', 'a')
        f.write(str(id)+';'+str(created_at)+';'+str(updated_at)+';'+text+'\n')
        f.close()
        return model.CreateNote(
            new_id=id,
        )
    else:
        return 'Неверный токен'


@app.patch('/update_note')
def update_note(id: int, text: str, token: str):
    #проверка токена
    if isCorrectToken(token):
        #заполнение list_notes
        add_to_list_notes()
        # поиск id
        if id not in id_notes:
            return 'Заметка с таким id не найдена'
        else:
            for i in range(len(id_notes)):
                if id == id_notes[i]:
                    #изменение списка
                    list_notes[i]['updated_at'] = datetime.datetime.now()
                    list_notes[i]['text'] = text+'\n'
                    write_to_file(list_notes)
                    return model.UpdateNote(
                        upd_id=id,
                        new_text=text
                    )
    else:
        return 'Неверный токен'


@app.delete('/delete_note')
def delete_note(id: int, token: str):
    #проверка токена
    if isCorrectToken(token):
        #заполнение list_notes
        add_to_list_notes()
        # поиск id
        if id not in id_notes:
            return 'Заметка с таким id не найдена'
        else:
            for i in range(len(id_notes)):
                if id == id_notes[i]:
                    #удаление из списков
                    id_notes.remove(id_notes[i])
                    list_notes.remove(list_notes[i])
                    write_to_file(list_notes)
                    return model.DeleteNote(
                        del_id=id,
                    )
    else:
        return 'Неверный токен'