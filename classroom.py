from gradebook import AliveStatus, Instructor, Student


class Classroom:
    def __init__(self):
        self.students_dict = {}
        self.instructors_dict = {}

    def add_instructor(self, inst: Instructor):
        key = len(self.instructors_dict) + 1

        if key not in self.instructors_dict.keys():
            self.instructors_dict[key] = inst

    def remove_instructor(self, key: int):
        del self.instructors_dict[key]

    def print_instructor(self):
        for key in self.instructors_dict:
            print(f'Key         : {key}')
            print(self.instructors_dict[key])

    def add_student(self, std: Student):
        key = len(self.students_dict) + 1

        if key not in self.students_dict.keys():
            self.students_dict[key] = std

    def remove_student(self, key: int):
        del self.students_dict[key]

    def print_student(self):
        print(self.students_dict)


if __name__ == "__main__":
    p1 = Student('Minnie', 'Mouse', '09091990', AliveStatus.ALIVE)
    p2 = Student('Donald','Duck', '04041990', AliveStatus.ALIVE)

    i1 = Instructor('Goofy', 'Doeshehavealastname', '05051998', AliveStatus.ALIVE)
    i2 = Instructor('Scrooge', 'McDuck', '02021970', AliveStatus.ALIVE)

    class1 = Classroom()
    class1.add_instructor(i1)
    class1.add_instructor(i2)

    print(len(class1.instructors_dict))

    #class1.remove_instructor(2)

    print(len(class1.instructors_dict))

    class1.print_instructor()


