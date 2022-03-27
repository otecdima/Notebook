"""Notebook"""
import datetime
import sys

class CommandOption:
    """command option"""
    pass

class Note:
    """Class note"""
    def __init__(self, memo, tags=''):
        """Init"""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

    def match(self, search_filter):
        """Function match"""
        if search_filter in self.memo:
            return True
        elif search_filter in self.tags:
            return True
        else:
            return False

class Notebook:
    """Class Notebook"""
    def __init__(self):
        """init"""
        self.notes = []

    def new_note(self, memo, tags=''):
        """function that create new note"""
        self.notes.append(Note(memo, tags))

    def find_note_by_filter(self, filter):
        """Function for finding note by filter"""
        try:
            for note in self.notes:
                if note.match(filter):
                    return f"Note with filter: {filter}:\n" +\
                           f" Memo: {note.memo}\n" +\
                           f" Tag: {note.tags}"
        except IndexError:
            return ('There is no note with that number')

    def find_note_by_number(self, number):
        """Function for finding note by number"""
        try:
            for note in self.notes:
                if self.notes[number-1] == note:
                    return f"Note with number: {number}:\n" +\
                           f"   Memo: {note.memo}\n" +\
                           f"   Tag: {note.tags}"
        except IndexError:
            return ('There is no note with that number')

    def modify_memo(self, note_number, memo):
        """Function to modify memo"""
        for note_ in range(1, len(self.notes)+1):
            if note_ == note_number:
                self.notes[note_-1].memo = memo
                break

    def modify_tags(self, note_number, tags):
        """Function to modify tags"""
        for note_ in range(1, len(self.notes)+1):
            if note_ == note_number:
                self.notes[note_-1].tags = tags
                break

class Menu():
    """Class Menu"""
    def __init__(self):
        """init"""
        self.notebook = Notebook()

    def display_menu(self):
        """Displays menu"""
        print("--------------\n"+\
        "Notebook Menu\n"+\
        "1. Show all Notes\n"+\
        "2. Search Notes\n"+\
        "3. Add Note\n"+\
        "4. Modify Note\n"+\
        "5. Quit\n"+\
        "--------------")

    def run(self):
        """Almost main function"""
        while True:
            self.display_menu()
            choice = int(input ("Enter an option: "))
            if choice == 1:
                print(self.show_notes())
            if choice == 2:
                self.search_note()
            if choice == 3:
                self.add_note()
            if choice == 4:
                self.modify_note()
            if choice == 5:
                print("Thank you for using your notebook!")
                sys.exit(0)

    def show_notes(self):
        """Function that show all notes"""
        if len(self.notebook.notes) == 0:
            return ("There is no available note in Notebook")
        for number in range(len(self.notebook.notes)):
            print(f"{number+1}: Memo: {self.notebook.notes[number].memo}\n"
                  f"   Tag: {self.notebook.notes[number].tags}")
        return ""

    def search_note(self):
        """search note"""
        if len(self.notebook.notes) == 0:
             return print("There is no available note to search in Notebook")
        print("If you want to search by filter enter 1, if by number enter 2")
        choice_ = int(input('Enter your choice: '))
        if choice_ == 1:
            number = int(input("Enter number of the note: "))
            return print(self.notebook.find_note_by_number(number))
        elif choice_ == 2:
            filter = input("Enter filter: ")
            return print(self.notebook.find_note_by_filter(filter))
        return ""

    def add_note(self):
        """Add note"""
        memo = input("Enter a memo: ")
        answer = input("Do you want to enter a tag?y/n: ")
        if answer == 'y':
            tag = input("Enter a tag: ")
            self.notebook.new_note(memo, tag)
        else:
            self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        """modify note"""
        if len(self.notebook.notes) == 0:
            return print("There is no available note to modify in Notebook")
        else:
            note_number = int(input("Enter a note number: "))
            while note_number > len(self.notebook.notes):
                print(f'There is no {note_number} note in the notebook')
                note_number = int(input("Enter a note number: "))
            memo = input("Enter a memo: ")
            tags = input("Enter tags: ")
            if memo:
                self.notebook.modify_memo(note_number, memo)
            if tags:
                self.notebook.modify_tags(note_number, tags)

if __name__ == "__main__":
    Menu().run()
