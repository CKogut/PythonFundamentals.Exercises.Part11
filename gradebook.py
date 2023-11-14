from enum import Enum


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