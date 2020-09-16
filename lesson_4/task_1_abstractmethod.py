from abc import abstractmethod, ABC
from datetime import datetime


class Person(ABC):
    all_person = []

    @abstractmethod
    def get_info_about_person(self):
        pass

    @abstractmethod
    def get_years(self):
        pass


class Enrollee(Person):

    def __init__(self, surname, date_of_birthday, faculty):
        self.surname = surname
        self.date_of_birthday = date_of_birthday
        self.faculty = faculty


    def get_info_about_person(self):
        return f'Enrollee: {self.surname} has birthday {self.date_of_birthday}, faculty - {self.faculty}'

    def get_years(self):
        symbols = [',', ';', ':', '/', '-']
        for _ in symbols:
            self.date_of_birthday = self.date_of_birthday.replace(_, '.')
        years_now = datetime.today() - datetime.strptime(self.date_of_birthday, '%Y.%m.%d')

        return int(years_now.days / 365.25)


class Student(Enrollee):

    def __init__(self, surname, date_of_birthday, faculty, course):
        super().__init__(surname, date_of_birthday, faculty)
        self.course = course


    def get_info_about_person(self):
        return f'Student: {self.surname} has birthday {self.date_of_birthday}, ' \
               f'faculty - {self.faculty}, course -{self.course}'


class Teacher(Enrollee):
    def __init__(self, surname, date_of_birthday, faculty, position, experience):
        super().__init__(surname, date_of_birthday, faculty)
        self.position = position
        self.experience = experience

    def get_info_about_person(self):
        return f'Student: {self.surname} has birthday {self.date_of_birthday}, ' \
               f'faculty - {self.faculty}, position - {self.position}, experience -{self.experience}'

