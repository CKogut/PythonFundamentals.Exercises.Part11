import unittest
from unittest import TestCase

import gradebook
from gradebook import AliveStatus, Person
from enum import Enum


class GradebookTest(unittest.TestCase):

    def setUp(self):
        self.expected_first_name = "Homer"
        self.expected_last_name = "Simpson"
        self.expected_dob = "01011980"
        self.expected_alive_status = AliveStatus.ALIVE
        self._homer = Person(self.expected_first_name, self.expected_last_name, self.expected_dob,
                             self.expected_alive_status)

    def test_person_init(self):
        self.assertEqual(self.expected_first_name, self._homer.first_name)
        self.assertEqual(self.expected_last_name, self._homer.last_name)
        self.assertEqual(self.expected_dob, self._homer.dob)
        self.assertEqual(self.expected_alive_status, self._homer.alive)

    def test_update_first_name(self):
        expected_first_name = "Bart"
        self._homer.update_first_name(expected_first_name)
        self.assertEqual(expected_first_name, self._homer.first_name)

    def test_update_last_name(self):
        expected_last_name = "Burns"
        self._homer.update_last_name(expected_last_name)
        self.assertEqual(expected_last_name, self._homer.last_name)

    def test_update_dob(self):
        expected_dob = "12311990"
        self._homer.update_dob(expected_dob)
        self.assertEqual(expected_dob, self._homer.dob)

