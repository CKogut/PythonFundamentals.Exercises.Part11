from enum import Enum
import uuid


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1


class Person:
    def __init__(self, first_name: str, last_name: str, dob: str, alive: AliveStatus):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def __str__(self):
        details = ''
        details += f'First name  : {self.first_name}\n'
        details += f'Last name   : {self.last_name}\n'
        details += f'DOB         : {self.dob}\n'
        details += f'Status      : {self.alive}\n'
        return details

    def update_first_name(self, name: str):
        self.first_name = name

    def update_last_name(self, name: str):
        self.last_name = name

    def update_dob(self, dob: str):
        self.dob = dob

    def update_alive_status(self, alive: AliveStatus):
        self.alive = alive


class Instructor(Person):
    def __init__(self, first_name: str, last_name: str, dob: str, alive: AliveStatus):
        super().__init__(first_name, last_name, dob, alive)

        pid = uuid.uuid4()
        self.instructor_id = 'instructor_' + str(pid)

    def __str__(self):
        details = ''
        details += f'First name  : {self.first_name}\n'
        details += f'Last name   : {self.last_name}\n'
        details += f'DOB         : {self.dob}\n'
        details += f'ID          : {self.instructor_id}\n'
        details += f'Status      : {self.alive}\n'
        return details


class Student(Person):
    def __init__(self, first_name: str, last_name: str, dob: str, alive: AliveStatus):
        super().__init__(first_name, last_name, dob, alive)

        pid = uuid.uuid4()
        self.student_id = 'student_' + str(pid)


class ZipCodeStudent(Student):
    pass  # no additional requirements were noted in the README for this class


class CollegeStudent(Student):
    pass  # no additional requirements were noted in the README for this class


