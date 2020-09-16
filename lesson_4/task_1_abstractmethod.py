from abc import abstractmethod, ABC
from datetime import datetime


class Person(ABC):

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_age(self):
        pass


class Enrollee(Person):

    def __init__(self, surname, date_of_birthday, faculty):
        self.surname = surname
        self.date_of_birthday = date_of_birthday
        self.faculty = faculty

    def get_info(self):
        return f'Enrollee: {self.surname} has birthday {self.date_of_birthday}, faculty: {self.faculty}'

    def get_age(self):
        symbols = [',', ';', ':', '/', '-']
        for _ in symbols:
            self.date_of_birthday = self.date_of_birthday.replace(_, '.')
        years_now = datetime.today() - datetime.strptime(self.date_of_birthday, '%Y.%m.%d')

        return int(years_now.days / 365.25)


class Student(Enrollee):

    def __init__(self, surname, date_of_birthday, faculty, course):
        super().__init__(surname, date_of_birthday, faculty)
        self.course = course

    def get_info(self):
        return f'Student: {self.surname} has birthday {self.date_of_birthday}, ' \
               f'faculty: {self.faculty}, course: {self.course}'


class Teacher(Enrollee):

    def __init__(self, surname, date_of_birthday, faculty, position, experience):
        super().__init__(surname, date_of_birthday, faculty)
        self.position = position
        self.experience = experience

    def get_info(self):
        return f'Teacher: {self.surname} has birthday {self.date_of_birthday}, ' \
               f'faculty: {self.faculty}, position: {self.position}, experience: {self.experience}'


list_of_person = [Enrollee('Kuznietsov', '1994:04:07', 'DOIT'),
        Student('Mark', '1984:03:16', 'DOIT', '1'),
        Teacher('Spilberg', '1974:05:16', 'DOIT', 'BIOLOGY', 10)]

for x in list_of_person:
    print(x.get_info())

year_from = int(input("year range from: "))
year_to = int(input("year range to "))

range_of_years_from_to = []
persons_years = []

for i in range(year_from, year_to):
    range_of_years_from_to.append(i)

for z in list_of_person:
    persons_years.append((z.get_age(), z.get_info()))

dict_persons_years = dict(persons_years)

for g in dict_persons_years.keys():
    if g in range_of_years_from_to:
        print(dict_persons_years[g])
