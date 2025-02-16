#task1
class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
def getemail(self):
    return f"{self.firstname}{self.lastname}@btu.eduge"
class Lector(People):
    def __init__(self, salary, firstname, lastname):
        super().__init__(firstname, lastname)
        self.salary = salary
    def getemail(self):
        return f"{self.firstname}{self.lastname}@btu.edu.ge"
class Student(People):
    def __init__(self, firstname, lastname, courses = []):
        super().__init__(firstname, lastname)
        self.courses = courses
def getemail(self):
    return f"{self.firstname}.{self.lastname}.1@btu.edu.ge"
human = People("Davit", "metrevelu")
        print(human.get_email())
child = Student("giorgi","yolbaia", ["biology", "programming", "physcs"])
        print(child.get_email())
Teacher = Lector("100$", "eka", "janadze")
    print(Teacher.getemail())
    #ragaca errorebs wers
        #task2
class LibraryItem:
    def __init__(self, title, subject):
        self.title = title
        self.subject = subject
        self.status = "available"
def booking(self):
        if self.status == "available":
            self.status = "occupied"
            print(f"{self.title} order.")
        else:
            print(f"{self.title} ordered.")
def __str__(self):
        return f"title: {self.title}, subject: {self.subject}, status: {self.status}"
class Book(LibraryItem):
    def __init__(self, title, subject, isbn, authors):
        super().__init__(title, subject)
        self.isbn = isbn
        self.authors = authors
    def __str__(self):
        return f"book - {super().__str__()}, isbn: {self.isbn}, authors: {', '.join(self.authors)}"
class cd(libraryitem):
    def __init__(self, title, subject):
        super().__init__(title, subject)
    def booking(self):
        print(f"cd "{self.title}" cannot order.")

    def __str__(self):
        return f"cd {super().__str__()}"
class magazine(LibraryItem):
    def __init__(self, title, subject, journal_name, volume):
        super().__init__(title, subject)
        self.journal_name = journal_name
        self.volume = volume
    def __str__(self):
        return f"magazine - {super().__str__()}, journal: {self.journal_name}, volume: {self.volume}"