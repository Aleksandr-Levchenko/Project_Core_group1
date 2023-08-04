from collections import UserDict
from datetime import datetime
import json

class Tag:
    def __init__(self, value=None):        
        self.__value = None
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value:
            self.__value = value

class Note(Tag):
    pass

class NoteRecord():
    def __init__(self, key: datetime, note: Note=None, tag: Tag=None):
        self.key = datetime.now()
        self.note = note
        self.tag = tag

    def __str__(self):
        return f"{str(self.key)}  {str(self.note) if self.note else ''}  {str(self.tag) if self.tag else ''}"
    
    def __repr__(self):
        return f"{str(self.key)}  {str(self.note) if self.note else ''}  {str(self.tag) if self.tag else ''}"
                
    def add_note(self, note:Note):
        self.note += note
        return f"Note {note} added."

    def del_note(self, note):
        self.note = ""
        return f"Note {note} deleted"

    def change_note(self, old_note: Note, new_note: Note):
        self.del_note(old_note)
        self.add_note(new_note)
        return f"Note {old_note} was replaced by {new_note}"

class NoteBook(UserDict):
    def add_record(self, record: NoteRecord):
        self.data[record.key] = record
        return f"Added new record {record}"
        
    def iterator(self, group_size):
        records = list(self.data.values())
        self.current_index = 0

        while self.current_index < len(records):
            group_items = records[self.current_index:self.current_index + group_size]
            group = [rec for rec in group_items]
            self.current_index += group_size
            yield group

    def save_data(self, filename):
        with open(filename, 'w') as f:
            json.dump({str(record.key): (str(record.note) if record.note else "", (str(record.tag) if record.tag else "")) for key, record in self.items()}, f)
        return f"The note_book is saved."

    def load_data(self, filename):
        try:
            with open(filename, 'r') as f:
                data_dict = json.load(f)
                for key, value in data_dict.items():
                    
                    note, tag = value[:-1], value[-1]

                    if tag:
                        record = NoteRecord(key, Note(note), Tag(tag))
                    else:
                        record = NoteRecord(key, Note(note))
                    self.data[record.key] = record

            if isinstance(self.data, dict):
                print(f"The note_book is loaded.")
            else:
                print("The file does not contain a valid note_book.")
        except FileNotFoundError as e:
            print(f"{e}")


    def find_note(self, fragment:str):
        count = 0
        result = ""
        for rec in self.values():
            line = str(rec) + "\n"
            if fragment in line.lower():
                result += line
                count += 1
        if result:
            result = f"The following {str(count)} records were found on the fragment '{fragment}' \n\n" + result
        else:
            result = f"No records was found for the fragment '{fragment}' \n"
        return result
    
if __name__ == "__main__":

    nb = NoteBook()
    file_name = "n_book.json"
    print(nb.load_data(file_name))
    print(nb) 
    key=datetime.now()
    note = Note('Create tag sorting')
    rec = NoteRecord(key, note, Tag('Project'))
    nb.add_record(rec)

    key=datetime.now()
    note = Note('Ще одна нотатка. Ні до чого')
    rec = NoteRecord(key, note, Tag('Нотатка'))
    nb.add_record(rec)

    print(nb.find_note('second'))
    print(nb.save_data(file_name))
    print(nb)