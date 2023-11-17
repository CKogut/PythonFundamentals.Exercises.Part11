from gradebook import AliveStatus, Instructor, Student


class Classroom:
    def __init__(self):
        self.students_dict = {}
        self.instructors_dict = {}

    def add_instructor(self, inst: Instructor):
        key = len(self.instructors_dict) + 1

        if key not in self.instructors_dict.keys():
            self.instructors_dict[key] = inst


if __name__ == "__main__":
    p1 = Student('Minnie', 'Mouse', '09091990', AliveStatus.ALIVE)
    p2 = Student('Donald','Duck', '04041990', AliveStatus.ALIVE)

    i1 = Instructor('Goofy', 'Doeshehavealastname', '05051998', AliveStatus.ALIVE)
    i2 = Instructor('Scrooge', 'McDuck', '02021970', AliveStatus.ALIVE)

    class1 = Classroom()
    class1.add_instructor(i1)
    class1.add_instructor(i2)

    print(len(class1.instructors_dict))

