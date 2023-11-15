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

        inst_id = uuid.uuid4()
        self.instructor_id = 'instructor_' + str(inst_id)


class Student(Person):
    def __init__(self, first_name: str, last_name: str, dob: str, alive: AliveStatus):
        super().__init__(first_name, last_name, dob, alive)

        st_id = uuid.uuid4()
        self.student_id = 'student_' + str(st_id)


class ZipCodeStudent(Student):
    pass

class CollegeStudent(Student):
    pass

class Classroom:
    def __init__(self):
        self.students = ()
        self.instructors = ()